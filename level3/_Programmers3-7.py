def solution(genres, plays):
    answer = []
    genreNumber = {}
    count = []
    index = 0
    for i in range(len(genres)):
        if genres[i] not in genreNumber:
            genreNumber[genres[i]] = index
            index += 1
        if len(count) > genreNumber[genres[i]]:
            count[genreNumber[genres[i]]].append([i,plays[i]])
        else:
            count.append([[i,plays[i]]])
    for j in range(len(count)):
        count[j] = sorted(count[j], key=lambda x:(-x[1], x[0]))
        count[j].append(sum(x[1] for x in count[j]))
    count = sorted(count, key=lambda x: x[-1], reverse=True)
    for k in range(len(count)):
        if len(count[k]) > 1:
            answer.append(count[k][0][0])
            answer.append(count[k][1][0])
        else:
            answer.append(count[k][0][0])
    print(genreNumber,count, answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
# genres = ['classic']
# plays = [500, 600, 150, 800, 2500]
plays = [500, 600, 500, 500, 2000]
# plays=[500]
# genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'zazz']
# plays = [500, 600, 150, 800, 2500, 1000]
# genres = ['classic', 'pop']
# plays = [1000,2000]
solution(genres, plays)