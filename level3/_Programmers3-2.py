def solution(N):
    answer = 0
    fib = [0,1]
    temp = 0
    for i in range(N):
        temp = fib[0]+fib[1]
        fib[0] = fib[1]
        fib[1] = temp
        answer = fib[0]*2+fib[1]*2
    return answer
solution(5)