const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const numbers = input[1].split(' ').map(Number);
const ans = [];
for (let i = 1;i<=Math.min(...numbers);i++){
  if(numbers.every((num)=> !(num % i))){
    ans.push(i);
  }
}
console.log(ans.join('\n'));