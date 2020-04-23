def solution(n):
    ans = 0
    fib = [0,1]
    if n in fib:
        return n
    for i in range(2,n+1):
            ans = (fib[0]+fib[1])%1234567
            fib[0] = fib[1]
            fib[1] = ans
    return ans