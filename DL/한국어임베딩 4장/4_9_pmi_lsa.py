# -*- coding: utf-8 -*-
"""4-9.PMI_LSA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jO43C7dEi6IUbJEyCVBNRQQJQUNjJSV9
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD

docs = ['성진과 창욱은 야구장에 갔다',
        '성진과 태균은 도서관에 갔다',
        '성진과 창욱은 공부를 좋아한다']

# 동시발생 빈도 행렬
count_model = CountVectorizer(ngram_range=(1,1))
x = count_model.fit_transform(docs)

word2idx = count_model.vocabulary_
idx2word = {v:k for k, v in word2idx.items()}

xc = x.T * x  # this is co-occurrence matrix in sparse csr format
xc.setdiag(0) # sometimes you want to fill same word cooccurence to 0
xc = xc.toarray()
print(xc)
idx2word

# 동시발생 결합확률 행렬
xp = xc / xc.sum()
xp

# PMI 행렬
# pmi = log[p(X_ij) / {p(X_i*) * p(X_*j)}]
def calc_pmi(cm):
    sum_col = cm.sum(axis=0)
    sum_row = cm.sum(axis=1)
    sum_tot = sum_col.sum()

    j_prob = np.outer(sum_row, sum_col) / sum_tot
    cm = cm / j_prob

    return np.log(cm + 1e-8)

pmi = calc_pmi(xp)
pmi

ppmi = pmi.copy()
ppmi[ppmi < 0] = 0.0
ppmi

# PMI matrix를 SVD로 분해한다.
# C = U.S.VT
# sklearn을 이용한 SVD 예시

# 특이값 (S)이 큰 4개를 주 성분으로 C의 차원을 축소한다.
svd = TruncatedSVD(n_components=4)
D = svd.fit_transform(pmi)

U = D / svd.singular_values_
S = np.diag(svd.singular_values_)
VT = svd.components_

print("\nU, S, VT :")
print(np.round(U, 2), '\n')
print(np.round(S, 2), '\n')
print(np.round(VT, 2), '\n')

print("C를 4개 차원으로 축소 : truncated (U * S)")
print(np.round(D, 2))

idx2word

