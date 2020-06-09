def solution(n):
    answer = 0
    binary = []
    binaryN = countOne(binary, n)
    n += 1
    while True:
        nextBinary = []
        currentCnt = countOne(nextBinary, n)
        if currentCnt == binaryN:
            return n
        n += 1

def countOne(binary, number):
    while number>1:
        binary.append(number%2)
        number //= 2
    return binary.count(1)