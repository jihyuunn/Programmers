function solution(s) {
    var answer = true;
    const nums = '0123456789';
    if (s.length ===4 || s.length===6) {
        for (const i of s) {
            if (!nums.includes(i)) {
                answer = false;
            }
    }
    } else {
        answer = false
    }
    return answer
}