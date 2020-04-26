function solution(clothes) {
    let answer = 1;
    const sort = {};
    for (const i of clothes) {
        let category = i[1];
        if (sort.hasOwnProperty(category)) {
            sort[category] += 1
        } else {
            sort[category] = 1
        }
    }
    for (const [key, value] of Object.entries(sort)) {
        answer *= (value+1)
    }
    return answer-1
}