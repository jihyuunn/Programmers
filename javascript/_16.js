function solution(numbers) {
    var answer = 0;
    const perm = [];
    const check = Array(numbers.length).fill(0);
    let temp = [];
    permutation(perm, temp, numbers, check);
    const prime = Array(10000000).fill(false);
    prime[0] = true;
    prime[1] = true;
    primeNumber(prime);
    for (const i of perm) {
        if (prime[i] == false) {
            answer += 1
        }
    }
    return answer;
}

function permutation(perm, temp, numbers, check) {
    if (!perm.includes(parseInt(temp.join(''))) && parseInt(temp.join(''))) {
        perm.push(parseInt(temp.join('')));
    };
    for (let i=0; i<numbers.length; i++) {
        if (check[i] === 0) {
            temp.push(numbers[i]);
            check[i] = 1;
            permutation(perm, temp, numbers, check);
            temp.pop();
            check[i] = 0;
        }
    };
}

function primeNumber(prime) {
    for (let i=2; i<5000000; i++) {
        let j=2;
        while (i*j < 10000000) {
            if (prime[i*j]===false) {
                prime[i*j] = true;
            }
            j += 1
        }
    }
}