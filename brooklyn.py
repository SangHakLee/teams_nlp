from gensim.models import FastText, KeyedVectors
import random
import re

def similar(self):
    #1. import a pretrained model
    model = KeyedVectors.load_word2vec_format('./data/wiki-news/wiki-brooklyn.bin', binary=True, unicode_errors='ignore')
    #print(model)
    sim1 = model.most_similar(self, topn = 25)
    # sim2 = '\n'.join([s[0] for s in sim1])
    return sim1

# print(similar('apple'))
