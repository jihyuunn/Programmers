function solution(n) {
    var answer = 0;
    const cntOne = convertBinary(0, n);
    n += 1;
    while (true) {
        let nextOne = convertBinary(0, n);
        if (nextOne === cntOne) {
            return n
        }
        n += 1;
    }
}

const convertBinary = (digits, number) => {
    while (number > 1) {
        if (number%2===1) {
            digits += 1;
        };
        number = parseInt(number/2)
    }
    return digits
}