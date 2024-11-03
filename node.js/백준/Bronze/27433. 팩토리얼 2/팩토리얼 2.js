const n = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

const factorial = (n) => {
    if (n < 2) return 1;
    return n * factorial(n-1)
}

console.log(factorial(n));