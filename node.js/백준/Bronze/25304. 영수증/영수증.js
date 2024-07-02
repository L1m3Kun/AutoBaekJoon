const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const total = Number(input[0]);

const ans = input.slice(2).reduce((acc, curr) => {
    const [price, item] = curr.split(' ').map(Number);
    return acc - (price*item);
}, total)
console.log(ans ? "No" : "Yes");