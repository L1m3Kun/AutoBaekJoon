const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const numbers = input[1].split(' ').map(Number);

const gcd = (a, b) => {
    while (b !== 0) {
        const tmp = a%b;
        a = b
        b = tmp;
    }
    return a;
}
const res = n > 2? gcd(gcd(numbers[0], numbers[1]), numbers[2]):gcd(numbers[0], numbers[1]);

const ans = [];
for (let i = 1 ; i <= Math.sqrt(res); i++){
    if (!(res % i)) {
        if (i !== res/i){
            ans.push(res/i);
        }
        ans.push(i);
    }
}
ans.sort((a,b) => a-b);
console.log(ans.join('\n'));