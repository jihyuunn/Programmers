def solution(name):
    answer = 0
    cnt=0
    cntA = 0
    index = len(name)
    for i in range(len(name)):
        if cnt == 0 and name[i] == 'A':
            cnt += 1
        elif name[i] == 'A' and name[i-1]=='A':
            cnt += 1
        elif cnt != 0 and name[i] != 'A':
            cntA = max(cntA, cnt)
            if cntA == cnt:
                index = i-cnt
            cnt = 0
    if cnt != 0:
        cntA = max(cntA, cnt)
        if cntA == cnt:
            index = len(name)-cnt
    print(index, cntA)
    if cntA == 0 or index > cntA:
        for j in name:
            if ord(j)-65 > 12:
                answer += 91-ord(j)
            else:
                answer += ord(j)-65
            answer += 1
        answer -= 1
        if name[-1] == 'A':
            answer -= cnt
    else:
        print(name[:index], name[index+cntA:])
        for k in name[:index]:
            if ord(k)-65 > 12:
                answer += 91-ord(k)
            else:
                answer += ord(k)-65
        answer += (index-1)*2 if index>0 else answer
        for i in name[index+cntA:]:
            if ord(i)-65 > 12:
                answer += 91-ord(i)
            else:
                answer += ord(i)-65
        answer += len(name[index+cntA:])
    print(answer)
    return answer if answer> -1 else 0
solution("BAABAAA")
solution("AAB")
solution("BAA")
solution("BAABAAAAAAB")
solution("AZAAAZ")
solution("BBBAAB")
solution('AAAA')
solution("JAN")
solution("BBBBAAABAAAB")