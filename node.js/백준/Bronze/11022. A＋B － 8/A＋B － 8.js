const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let answer = '';
input.slice(1).forEach((e,index) => {
    const [a, b] = e.split(' ').map(Number);
    answer += `Case #${index+1}: ${a} + ${b} = ${a+b}\n`;
});
console.log(answer);