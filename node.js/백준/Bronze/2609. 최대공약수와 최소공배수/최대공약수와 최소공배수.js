const fs = require('fs');
const [a,b] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const gcd = (a, b) => {
    while( b>0) {
        [a,b] = [b, a%b];
    }
    return a
}

const lcm = (a,b) => Math.floor(a*b / gcd(a,b));

console.log([gcd(a,b), lcm(a,b)].join('\n'));