# -*- coding: utf-8 -*-
"""4-10.sentece_piece.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nGJ5pqTn_JgsEBMOBknfxYLy5E_9159T
"""

!pip install sentencepiece

# Google의 Sentencepiece를 이용해서 챗-봇용 학습 문장을 subword token으로
# 분해한다.
#
# 코드 구현 : blog.naver.com/chunjein, 2021.03.31
# ----------------------------------------------------------------------
import pandas as pd
import sentencepiece as spm  # pip install sentencepiece
import re
import pickle

# Commented out IPython magic to ensure Python compatibility.
# 챗-봇 데이터 파일을 읽어온다.
# %cd '/content/drive/MyDrive/Colab Notebooks/'
corpus = pd.read_csv('data/ChatBotData.csv', header=0, encoding='utf-8')

# 질문과 답변을 합쳐서 subword vocabulary를 만든다.
corpusQA = list(corpus['Q']) + list(corpus['A'])

# 특수 문자를 제거한다.
corpusQA = [re.sub("([~.,!?\"':;)(])", "", s) for s in corpusQA]
corpusQA[:10]

corpus.head()

# Sentencepice용 사전을 만들기 위해 corpusQA를 저장해 둔다.
data_file = "data/chatbot_data.txt"
with open(data_file, 'w', encoding='utf-8') as f:
    for sent in corpusQA:
        f.write(sent + '\n')

# Google의 Sentencepiece를 이용해서 vocabulary를 생성한다.
# -----------------------------------------------------
templates= "--input={0:} \
            --pad_id=0 --pad_piece=<PAD>\
            --unk_id=1 --unk_piece=<UNK>\
            --bos_id=2 --bos_piece=<START>\
            --eos_id=3 --eos_piece=<END>\
            --model_prefix={1:} \
            --vocab_size={2:}"

VOCAB_SIZE = 9600
model_prefix = "data/chatbot_model"
params = templates.format(data_file, model_prefix, VOCAB_SIZE)

spm.SentencePieceTrainer.Train(params)
sp = spm.SentencePieceProcessor()
sp.Load(model_prefix + '.model')

with open(model_prefix + '.vocab', encoding='utf-8') as f:
    vocab = [doc.strip().split('\t') for doc in f]

word2idx = {k:v for v, [k, _] in enumerate(vocab)}
idx2word = {v:k for k, v in word2idx.items()}

word2idx

# string으로 조회
sentence = corpusQA[610]
enc = sp.encode_as_pieces(sentence)
dec = sp.decode_pieces(enc)

print('\n    문장:', sentence)
print('Subwords:', enc)
print('    복원:', dec)

# 수동 decode
print(''.join([x.replace('▁', ' ') for x in enc])[1:])

# word index로 조회
idx = sp.encode_as_ids(sentence)
dec = sp.decode_ids(idx)

print('\n    문장:', sentence)
print('Subwords:', idx)
print('    복원:', dec)

# word index로 변환한다.
corpusQA_idx = [sp.encode_as_ids(qa) for qa in corpusQA]

corpusQA_idx[0]

corpusQA[0]

idx2word[4312]

