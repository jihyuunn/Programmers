import string
def solution(msg):
    answer = []
    words = {}
    upper = string.ascii_uppercase
    print(upper)
    for i in upper:
        words[i] = ord(i)-64
    left = 0
    right = 1
    current = ''
    number = 27
    while left < right and left<= len(msg)-1:
        current += msg[left]
        print(current, left, right)
        if current + msg[right] in words:
            # current += msg[right]
            right = min(right+1, len(msg)-1)
            left += 1
        else:
            print(answer, current)
            words[current + msg[right]] = number
            number+=1
            answer.append(words[current])
            current = ''
            left = right
            right = min(left+1, len(msg)-1)
            # right = left+1
    if current == '':
        answer.append(words[msg[-1]])
    else:
        answer.append(words[current+msg[-1]])
    print(answer, words, current)
    return answer

# msg = "KAKAO"
msg = "TOBEORNOTTOBEORTOBEORNOT"
# msg = "ABABABABABABABAB"
solution(msg)
