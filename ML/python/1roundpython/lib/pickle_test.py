#피클이라는 저장방식
import pickle
                          
# # 객체를 파일로 저장        wb : write binary
# with open('pickle_test.txt','wb') as f:
#     data = {1:'python', 2:'javascript'}
#     pickle.dump(data, f)

# 객체를 불러오기             rb : read binary
with open('pickle_test.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)