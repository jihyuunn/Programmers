def solution(s):
    answer = ''
    index = 0
    current = 0
    s = s.lower()
    while index < len(s):
        if s[index] != ' ':
            if current%2 == 0:
                answer += chr(ord(s[index])-32)
            else:
                answer += s[index]
            current += 1
        else:
            answer += ' '
            current = 0
        index += 1
    return answer

def solution(s):
    return ' '.join(''.join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(w)]) for w in s.split(' '))