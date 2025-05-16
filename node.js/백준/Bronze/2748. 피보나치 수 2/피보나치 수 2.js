const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString());

const solution = (n) => {
    if (n < 3) return 1;
    const fibo = Array.from({length: n+1}, () => 0n);
    fibo[1] = 1n;
    for (let i = 2; i <= n; i++){
        fibo[i] = BigInt(fibo[i-1]) + BigInt(fibo[i-2]);
    }
    return fibo[n];
}

console.log(solution(input).toString().slice(0));