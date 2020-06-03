import heapq
def solution(operations):
    answer = [0,0]
    q = []
    for i in operations:
        order, num = i.split(' ')
        if order == 'I':
            q.append(int(num))
        elif order == 'D' and q:
            q = delete(num, q)
    if q:
        q = sorted(q)
        answer = [q[-1], q[0]]
    return answer

def delete(num, q):
    if num == '1':
        q = sorted(q)
        q.pop()
        return q
    else:
        q = sorted(q, reverse=True)
        q.pop()
        return q