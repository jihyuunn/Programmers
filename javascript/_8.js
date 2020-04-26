function solution(array, commands) {
    var answer = [];
    for (let i of commands) {
        const cur = array.slice(i[0]-1, i[1]);
        cur.sort(function(a, b){return a - b})
        answer.push(cur[i[2]-1]);
    }
    return answer;
}