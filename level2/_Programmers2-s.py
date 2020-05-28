def solution(w,h):
    answer = w+h-getGCD(w,h)
    return w*h-answer

def getGCD(w,h):
    print(w,h)
    if h == 0:
        return w
    return getGCD(h, w%h)