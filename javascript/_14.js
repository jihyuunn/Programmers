function solution(number, k) {
    var answer = '';
    let index = 0;
    let total = number.length-k
    while (k>0) {
        let current = number.slice(index, index+k+1);
        let maxNum = '0';
        for (let i=0; i<current.length;i++) {
            maxNum = maxNum<current[i]?current[i]:maxNum;
            if (maxNum === '9') break
        }
        answer += maxNum;
        index += current.indexOf(maxNum)+1;
        k -= current.indexOf(maxNum);
        if (answer.length==total) {
            return answer
        }
    }
    while (answer.length<total) {
        answer += number[index]
        index += 1
    }
    return answer;
}