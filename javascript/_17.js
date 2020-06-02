function solution(citations) {
    let answer = 0;
    citations.sort((a,b) => b-a);
    for (let i=0;i<citations.length;i++) {
        let temp = Math.min(citations[i], i+1);
        answer = Math.max(answer, temp)
    }
    return answer
}