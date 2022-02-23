import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

actual = [1,0,1,1,0,0,1,0]
predicted = [1,0,0,0,0,1,1,0]

matrix = confusion_matrix(actual, predicted, labels=[1,0])
print('Confusion matrix : \n', matrix)

tp, fn, fp, tn = confusion_matrix(actual,predicted,labels=[1,0]).reshape(-1)
print('Outcome values : \n', tp, fn, fp, tn)

matrix = classification_report(actual, predicted, labels=[1,0])
print('Clssification report:\n', matrix)



# 강사님 풀이

import numpy as np

y_test = np.array([1, 0, 1, 1, 0, 0, 1, 0])
y_prob = np.array([0.8, 0.2, 0.4, 0.4, 0.3, 0.6, 0.7, 0.1])

# 추정 확률로 label을 결정한다.
def find_label(p, treshold = 0.5):
    label = (p > treshold).astype('uint8')
    return label

y_pred = find_label(y_prob, 0.5)

# Confusion matrix를 생성한다
cm = np.zeros([2, 2])
for a in [0, 1]:
    idx = np.where(y_test == a)
    for p in [0, 1]:
        cm[a, p] = (y_pred[idx] == p).sum()

# 평가 지표들을 계산한다.
tn = cm[0, 0]
fp = cm[0, 1]
fn = cm[1, 0]
tp = cm[1, 1]

accuracy = (tn + tp) / cm.sum()
precision = tp / cm[:, 1].sum()
recall = tp / cm[1, :].sum()
f1 = 2 * precision * recall / (precision + recall)

print(cm)
print('\naccuracy = %.3f' % accuracy)
print('precision =  %.3f' % precision)
print('recall =  %.3f' % recall)
print('f1 =  %.3f' % f1)



from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print(classification_report(y_test, y_pred))

print(' Accuracy = %.3f' % accuracy_score(y_test, y_pred))
print('   Recall = %.3f' % recall_score(y_test, y_pred, average='macro'))
print('Precision = %.3f' % precision_score(y_test, y_pred, average='macro'))
print(' F1-score = %.3f' % f1_score(y_test, y_pred, average='macro'))

