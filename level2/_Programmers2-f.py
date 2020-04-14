def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print([x*3 for x in numbers])
    return ''.join(numbers)
    

numbers = [3, 30, 34, 5, 9, 1]
# numbers = [341,342]
# numbers = [0,0,0]
solution(numbers)