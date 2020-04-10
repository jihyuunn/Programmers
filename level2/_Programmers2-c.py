import string
def solution(s):
    answer = ''
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    index = 0
    first = True
    while index <= len(s)-1:
        if first == True:
            if s[index] in lower:
                answer += s[index].upper()
                first = False
            else:
                answer += s[index]
                first = False
        else:
            if s[index] in upper:
                answer += s[index].lower()
            else:
                answer += s[index]
        if s[index] == ' ':
            first = True
        index += 1
    print(answer)
    return answer

# s = "  for the last week  "
# s = "3people unFollowed me for the last week"
s = 'AA    AAA BBBB'
solution(s)