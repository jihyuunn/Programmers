def solution(n):
    for i in range(1, n//2+1):
        if n%i==0:
            n += i
            print(n)
    return n
# 이렇게 코드를 짜면 n이 계속 갱신되기 때문에 정답이 안나온다
def solution(n):
    answer = [i for i in range(1,n//2+1) if n%i==0]
    return n+sum(answer)
    
solution(5)