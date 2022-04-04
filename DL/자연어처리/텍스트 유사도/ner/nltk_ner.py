# -*- coding: utf-8 -*-
"""8-4.nltk_NER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Px6uzt8wLYrW_jEVGigfrJ2PtKanhbmL
"""

import nltk

nltk.download('treebank')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Named Entity Recognition (NER)
sent = nltk.corpus.treebank.tagged_sents()[1]

print(sent)

print(nltk.ne_chunk(sent, binary=True))

print(nltk.ne_chunk(sent, binary=False))

