import string
def solution(s, n):
    answer = ''
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    for char in s:
        cur = ord(char)+n
        if char in upper:
            if cur > 90:
                cur -= 26
        elif char in lower:
            if cur > 122:
                cur -= 26
        else:
            cur -= n
        answer += chr(cur) 
    return answer