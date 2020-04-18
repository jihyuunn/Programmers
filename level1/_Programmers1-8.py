def solution(n):
    answer = ''
    remain = [0,1,2,4,11,12,14,21,22,24,41]
    temp = ''
    answer = go(n, remain, temp)
    return answer

def go(n, remain, temp): 
    if 0 < n <= 10:
        return str(remain[n])
    if n%3 == 0:
        temp += go(n//3-1, remain, temp)
        temp += '4'
    else:
        temp += go(n//3, remain, temp)
        temp += go(n%3, remain, temp)
    return temp
solution(3)