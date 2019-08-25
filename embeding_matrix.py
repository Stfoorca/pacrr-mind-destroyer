from gensim.test.utils import datapath
from gensim.models import KeyedVectors
import glob
import shutil
import re
import numpy as np
import os

def stop_char_remove(string):
    characters = '!@#$%^&*()_+1234567890-=[];\',./{}:\"<>?\n'
    for character in characters:
        string = string.replace(character, '')

    return string

def get_name(path):
    pattern = r'.*\/(\d+)'
    renamedPath = re.search(pattern, path).group(1)
    if renamedPath[0]=='0':
        renamedPath = renamedPath[1:]
    return renamedPath


def get_clear_tokens(path_to_data): 
    for file in glob.glob(path_to_data):
        with open(file, 'r') as f:
            data = f.read()
            data = stop_char_remove(data)
            yield [data.split(' '), file]

def max_len(path_to_data):
    to_return = 0

    for item, _ in get_clear_tokens(path_to_data):
        to_return = max(to_return, len(item))

    return to_return

def generate_matrix(path_to_data, path_to_query):
    max_doc = max_len(path_to_data)
    max_query = max_len(path_to_query)

    print('Document max size: {}'.format(max_doc))
    print('Query max size: {}'.format(max_query))
    model = KeyedVectors.load_word2vec_format('./model.bin', binary=True)
    counter = 0
    for doc_data in get_clear_tokens(path_to_data):
        doc_name = get_name(doc_data[1])
        if counter % 1000 == 0:
            print('Counter: {}'.format(counter))
        counter += 1
        for query_data in get_clear_tokens(path_to_query):
            array = np.zeros((len(query_data[0]), len(doc_data[0])), dtype='float64')
            for i, doc_word in enumerate(doc_data[0]):
                for j, query_word in enumerate(query_data[0]):
                    try:
                        array[j][i] = model.similarity(doc_word, query_word)
                    except Exception as e:
                        array[j][i] = 0

            np.save('./cosine/topic_doc_mat/{}/{}.npy'.format(get_name(query_data[1]), doc_name), array)



generate_matrix('/home/pepe/Desktop/paccr-master/relevant/*', '/home/pepe/Desktop/paccr-master/query/*')