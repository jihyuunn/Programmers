def solution(board):
    answer = 1
    onlyzero = True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                onlyzero = False
                temp = check(board, i, j)
                if temp != 0:
                    board[i][j] = temp+1
                    answer = max(answer, temp+1)
    if onlyzero == True:
        return 0
    return answer**2
def check(board, i, j):
    if i>0 and j>0:
        first = board[i][j-1]
        second = board[i-1][j]
        third = board[i-1][j-1]
        if first!=0 and second!=0 and third!=0:
            return min(first, second, third)
    return 0
solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])