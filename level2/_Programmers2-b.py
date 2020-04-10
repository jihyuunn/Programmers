def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        index = 0
        no = False
        for i in tree:
            if i in skill:
                if skill.index(i) > index:
                    no = True
                    break
                else:
                    index += 1
        if no == False:
            answer += 1
    print(answer)
    return answer
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)