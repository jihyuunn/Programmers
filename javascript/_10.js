function solution(numbers) {
    let answer = numbers.sort((a, b) => `${b}${a}` - `${a}${b}`).join('');
    return answer[0] === '0' ? '0' : answer;
}

function solution(numbers) {
    var answer = '';
    numbers.sort(function(a,b) {return String(a).repeat(3)<String(b).repeat(3)})
    for (const i of numbers) {
        answer += String(i)
    }
    return String(parseInt(answer))
}