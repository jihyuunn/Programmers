function solution(participant, completion) {
    var answer = '';
    let cnt = {}
    for (let i=0; i<participant.length; i++) {
        if (participant[i] in cnt) {
            cnt[participant[i]] += 1
        } else {
            cnt[participant[i]] = 1
        }
    }
    for (let j=0; j<completion.length; j++) {
        cnt[completion[j]] -= 1
    }
    for (const [key,value] of Object.entries(cnt)) {
        if (value === 1) {
            return key
        }
    }
}