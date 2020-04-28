def solution(arr):
    while len(arr) > 1:
        first = arr.pop()
        second = arr.pop()
        if first > second:
            first, second = second, first
        arr.append(first*second//gcd(second, first))
    return arr[0]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
solution([2,6,8,14])