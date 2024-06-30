const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const testCase = Number(input[0]);
const answer = [];

input.slice(1).forEach((e) => {
    const [a, b] = e.split(' ').map(Number);
    answer.push(a+b);
});
console.log(answer.join("\n"));