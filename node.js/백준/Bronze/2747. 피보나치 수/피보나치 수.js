const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString());

const solution = (n) => {
    if (n < 1) return 0;
    if (n < 3) return 1;
    const fibo = Array.from({length: n+1}, () => 0);
    [fibo[0], fibo[1]] = [0, 1];
    for (let i = 2; i <= n; i++){
      fibo[i] = fibo[i-1] + fibo[i-2];  
    }
    return fibo[n];
}

console.log(solution(input));