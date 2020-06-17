def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        if word == '':
            answer += ' '
        else:
            word = word[0].upper()+word[1:].lower()
            answer += word+' '
    return answer[:-1]