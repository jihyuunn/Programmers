def solution(strings, n):
    answer = []
    strings.sort()
    strings = sorted(strings, key=lambda x: x[n])
    print(strings)
    return answer

solution(['abzcd','cdzab','abzfg','abzaa','bbzaa','abzbb'], 2)