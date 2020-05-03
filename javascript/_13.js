function solution(priorities, location) {
    var answer = 0;
    while (priorities.length > 0) {
        let current = priorities.shift();
        let printed = true;
        for (let i=0; i<priorities.length; i++) {
            if (current < priorities[i]) {
                priorities.push(current);
                printed= false;
                break;
            }
        }
        console.log(current, location, printed)
        if (location === 0 && printed) {
            return answer+1
        } else if (location===0 && !printed) {
            location = priorities.length-1
        } else if (printed) {
            answer += 1
            location -= 1
        } else {
            location -= 1
        }
    }
}