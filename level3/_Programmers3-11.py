def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            current = 0
            for k in range(len(arr1[0])):
                current += arr1[i][k]*arr2[k][j]
            temp.append(current)
        answer.append(temp)
    return answer

def productMatrix(X, Y):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer