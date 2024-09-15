const fs = require('fs');
let [a,b,c] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(BigInt);

let ans = 1n;
while (b > 0) {
    if (b % 2n) {
        ans *= a;
        ans %= c;
    }
    a *= a;
    a %= c;
    
    b >>= 1n;
}

console.log(Number(ans));