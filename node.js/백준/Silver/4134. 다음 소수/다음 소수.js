const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const isPrime = (n) => {
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (!(n%i)) return false;
    } 
    return true;
}

const solution = (N) => {
    if ( N <= 2 ) return 2;
    for (let i = N; i <= N*2; i ++){
        if (isPrime(i)) return i;
    }
}

const main = (testCase) => {
    const ans = testCase.map(n => solution(n));
    console.log(ans.join('\n'));
}

main(input.slice(1));