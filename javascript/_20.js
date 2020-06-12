function solution(n, times) {
    var answer = 0;
    let left = 0;
    let right = Math.max(...times)*n;
    let temp = 0;
    while (left <= right) {
        let mid = parseInt((left+right)/2);
        temp = 0;
        for (const i of times) {
            temp += parseInt(mid/i)
        }
        if (temp < n) {
            left = mid+1
        } else {
            answer = mid;
            right = mid -1;
        }
    }
    return answer;
}