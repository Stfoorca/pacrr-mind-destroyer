from time import time
from gensim.models import Word2Vec
import multiprocessing
from collections import defaultdict
import glob
from gensim.parsing.preprocessing import remove_stopwords

document_direcotry = 'relevant/*'

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

def build_corpus(path_to_data_folder):
    corpus = []
    for file in glob.glob(path_to_data_folder):
        with open(file, 'r') as f:
            content = f.read()
            corpus.append(data_normalization(content).split(' '))

    frequency = defaultdict(int)

    for doc in corpus:
        for token in doc:
            frequency[token] += 1

    return [[token for token in doc if frequency[token] > 1] for doc in corpus]

def train(path_to_data, model_path, epoch, binary):
    print('Started training model')
    cores = multiprocessing.cpu_count()
    t = time()
    w2v_model = Word2Vec(min_count=20,
                         window=2,
                         size=300,
                         sample=6e-5,
                         alpha=0.03,
                         min_alpha=0.0007,
                         negative=40,
                         workers=cores-2)
    sentences = build_corpus(path_to_data)
    w2v_model.build_vocab(sentences, progress_per=1000)
    print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))

    t = time()
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=epoch, report_delay=1)

    print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))

    w2v_model.wv.save_word2vec_format(model_path, binary=binary)
    print('Model saved')

train(document_direcotry, './model.bin', 40, True)