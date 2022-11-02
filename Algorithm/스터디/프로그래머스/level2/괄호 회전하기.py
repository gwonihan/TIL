# 괄호 회전하기
def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        st = []
        
        for i in range(len(s)):
            
            if len(st) > 0:
                if st[-1] == '[' and s[i] == ']':
                    st.pop()
                elif st[-1] == '(' and s[i] == ')':
                    st.pop()
                elif st[-1] == '{' and s[i] == '}':
                    st.pop()
                else:
                    st.append(s[i])
            else:
                st.append(s[i])
        
        if len(st) == 0:
            answer += 1
        a = s[0]
        s = s[1:]
        s += a
    
    return answer