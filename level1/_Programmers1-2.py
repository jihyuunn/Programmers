import string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
def solution(s):
    answer = ''
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] in lower:
                answer += chr(ord(s[i])-32)
            else:
                answer += s[i]
        else:
            if s[i] in upper:
                answer += chr(ord(s[i])+32)
            else:
                answer += s[i]
    print(answer)
    return answer
solution("try hello world")