from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    check = [0]*(len(words))
    q = deque()
    q.append(0)
    answer = bfs(check, q, words, begin, target)
    print(answer)
    return answer

def bfs(check, q, words, current, target):
    while q:
        t = q.popleft()
        print(q, check, t, current)
        for i in range(len(words)):
            if check[i] < check[t]+1:
                temp = words[i]
                diff = 0
                for j in range(len(temp)):
                    if temp[j] != current[j]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    if temp == target:
                        return check[t]+1
                    else:
                        check[i] = check[t]+1
                        q.append(i)
        current = words[q[0]]

begin = "hit"
# begin = 'hhhhh'
target = "cog"
# target = 'hhh'
# target = 'hhhtt'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ['hhh', 'hht']
# words = ['hhhht', 'hhhtt']
solution(begin, target, words)