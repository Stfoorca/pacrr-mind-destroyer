import re
# from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import remove_stopwords

from shutil import copy2

begin_docid_token = '<docid>'
end_docid_token = '</docid>'

begin_body_token = '<body>'
end_body_token = '</body>'

def stop_char_remove(string):
    characters = '!@#$%^&*()_+1234567890-=[];\',./{}:\"<>?'
    for character in characters:
        string = string.replace(character, ' ')

    string = string.split(' ')

    return ' '.join([token for token in string if len(token) > 1])


def data_normalization(data):
    data = data.lower()
    data = stop_char_remove(remove_stopwords(data))
    return data

def prepare_data(path_to_docs, path_to_qrels):
    print('Started preparing data')
    relevant_files = []

    with open(path_to_qrels, 'r') as file:
        qrels = file.read()
    qrels = qrels.split('\n')

    # regex101.com
    #regex = r'(\d+)\s(\d+)\s(\d+)\s([+|-]?\d+\$)'

    for line in qrels:
        #data = re.search(regex, line)

        tmp = line.split('\t')
        data = []
        for string in tmp:
            string = string.replace(' ', '')
            data.append(string)
        is_relevant = data[3]

        if is_relevant != '-1':
            file_name = data[2]
            relevant_files.append(file_name)

    for i in range(0, len(relevant_files)):
        file_name = path_to_docs + relevant_files[i]
        if i % 500 == 0:
            print('Counter: {}'.format(i))
        with open(file_name, 'r') as file:
            data = file.read()

            docid = data[data.find(begin_docid_token) + len(begin_docid_token):data.find(end_docid_token)]

            data = data[data.find(begin_body_token) + len(begin_body_token):data.find(end_body_token)]

            with open('./relevant/' + docid, 'w') as copy_file:
                copy_file.write(data_normalization(data))

 # filtered_sentence = [w for w in word_tokens if not w in stop_words]
            if docid != relevant_files[i]:
                assert 1 == 0
    print('Data prepared')


prepare_data('./docs/', './qrels')