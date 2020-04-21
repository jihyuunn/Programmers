def solution(numbers):
    temp = ''
    c = [False]*len(numbers)
    go(9999999)
    makeNumber(c, numbers, temp, [])
    return answer

def makeNumber(c, numbers, temp, ans):
    global answer, check
    if len(temp)>0 and int(temp) not in ans:
        ans.append(int(temp))
        if check[int(temp)] == False:
            answer += 1
    for i in range(len(numbers)):
        if c[i] == False:
            c[i] = True
            makeNumber(c, numbers, temp+numbers[i], ans)
            c[i] = False
        
def go(number):
    global check
    i = 2
    for i in range(2, number//2):
        j = 2
        if check[i] ==True:
            continue
        while i*j < number:
            check[i*j] = True
            j+=1
answer = 0
check = [True,True]+[False]*9999998
solution("123")