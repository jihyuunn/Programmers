function solution(n) {
    var answer = '';
    const numbers = ['0','1','2','4']
    if (n <= 3) {
        return numbers[n]+answer
    }
    const last = Math.ceil(n%3)==0?numbers[3]:numbers[Math.ceil(n%3)];
    console.log(last);
    answer = answer+last
    if (Math.ceil(n%3)==0) {
        answer= solution(n/3-1)+answer
    } else {
        answer= solution(Math.floor(n/3))+answer
    }
    return answer
}