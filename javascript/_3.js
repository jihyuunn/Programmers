function solution(s){
    var answer = true;
    const strings = s.toLowerCase();
    let cntP = 0
    let cntY = 0
    for (const i of strings) {
        if (i === 'p') {
            cntP += 1
        } else if (i === 'y') {
            cntY += 1
        }
    }
    if (cntP === cntY) {
        return answer;
    } else {
        return false
    }
}