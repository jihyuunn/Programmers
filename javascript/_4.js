function solution(s) {
    var answer = '';
    const n = s.length
    if (n%2==0) {
        return s.slice(n/2-1,n/2+1)
    }
    return s.slice(n/2, n/2+1);
}

function solution(s) {
    var answer = '';
    const n = Math.floor(s.length/2);
    return s.length%2===0 ? s[n-1]+s[n]:s[n];
}