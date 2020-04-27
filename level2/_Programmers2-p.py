def solution(n, computers):
    global check
    answer = 0
    current = 1
    for i in range(n):
        if check[i] == 0:
            dfs(computers, i, current)
            current+=1
    print(current)
    return current-1

def dfs(computers, i, current):
    global check
    for j in range(len(computers[i])):
        if check[j] == 0 and computers[i][j]==1:
            check[j] = current
            dfs(computers, j, current)
n = 3
check = [0]*n
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n,computers)