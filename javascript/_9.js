function solution(progresses, speeds) {
    const answer = [];
    const days = []
    for (let i = 0;i<speeds.length;i++) {
        days.push(Math.ceil((100-progresses[i])/speeds[i]))
    }
    let temp = 1
    let maxdays = days[0]
    for (let j = 1;j<days.length;j++) {
        if (maxdays < days[j]) {
            answer.push(temp)
            temp = 1
            maxdays = days[j]
        } else {
            temp += 1
        }
    }
    answer.push(temp)
    return answer;
}
solution([99,99,99,99], [1,1,1,1])