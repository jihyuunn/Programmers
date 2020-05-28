from collections import deque
def solution(n, edge):
    vertex = {}
    check = [0]*(n+1)
    for node in edge:
        x, y = node
        if x in vertex:
            vertex[x].append(y)
        else:
            vertex[x] = [y]
        if y in vertex:
            vertex[y].append(x)
        else:
            vertex[y] = [x]
    d = deque()
    d.append(1)
    check[1] = 1
    bfs(check, vertex, d)
    distance = max(check)
    return check.count(distance)

def bfs(check, vertex, d):
    while d:
        temp = d.popleft()
        for i in vertex[temp]:
            if check[i] == 0:
                check[i] = check[temp]+1
                d.append(i)