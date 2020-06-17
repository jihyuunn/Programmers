function solution(A,B){
    var answer = 0;
    let a = A.sort((a,b) => a-b)
    let b = B.sort((a,b) => b-a)
    // console.log(A,B)
    for (let i=0;i<a.length;i++) {
        answer += a[i]*b[i]
    }
    return answer;
}