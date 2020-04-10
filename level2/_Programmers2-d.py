def solution(p):
    answer = ''
    print(p)
    if right(p):
        # answer += p
        return p
    else:
        index = 0
        check = 0
        while True:
            if p[index] == '(':
                check += 1
            else:
                check -= 1
            if check == 0:
                break
            index += 1
        u, v = p[:index+1], p[index+1:]
        print(u,v)
        if right(u):
            current = u + solution(v)
            return current
        else:
            current = '('
            current += solution(v)+')'
            print(current, 'c')
            u = u[1:-1]
            for j in u:
                if j == '(':
                    current += ')'
                else:
                    current += '('
            return current   
    return answer

def right(u):
    openn = []
    for i in u:
        if i == '(':
            openn.append(i)
        else:
            if openn:
                openn.pop()
    if len(openn) > 0:
        return False
    return True

def balance(u):
    check = 0
    for i in u:
        if i == '(':
            check += 1
        else:
            check -= 1
    if check == 0:
        return True
    return False

p = ')('
# p = "(()())()"
# p = "()))((()"
print(solution(p))