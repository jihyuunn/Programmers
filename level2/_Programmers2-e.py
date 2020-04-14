# 프린터
from collections import deque
def solution(priorities, location):
    answer = 0
    important = max(priorities)
    priorities = deque(priorities)
    while priorities:
        print(priorities, location)
        current = priorities.popleft()
        if current == important:
            important = max(priorities)
            answer += 1
            if location == 0:
                print(answer)
                return answer
        else:
            priorities.append(current)
        if location == 0:
            location = len(priorities)-1
        else:
            location -= 1
    return answer

# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0
solution(priorities, location)