function solution(arrangement) {
    var answer = 0;
    const open = [];
    for (let i=0; i<arrangement.length; i++) {
        if (arrangement[i] === ')') {
            if (arrangement[i-1] === '(') {
                open.pop();
                answer += open.length;
            } else {
                answer += 1;
                open.pop();
            }
        } else {
            open.push('(');
        }
    }
    return answer;
}