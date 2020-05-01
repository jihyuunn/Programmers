function solution(heights) {
    var answer = [];
    for (let i=heights.length-1;i>-1;i--) {
        let current = heights[i];
        let isSend = false;
        for (let j=i-1;j>-1;j--) {
            if (current<heights[j]) {
                answer.push(j+1)
                isSend = true;
                break
            }
        }
        if (isSend === false) {
            answer.push(0)
        }
    }
    return answer.reverse();
}