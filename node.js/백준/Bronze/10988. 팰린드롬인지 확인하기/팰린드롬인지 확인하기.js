const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
let isPalin = true;
for (let i =0; i<Math.floor(input.length/2);i++) {
    if (input[i] !== input[input.length-i-1]){
        isPalin = false;
    }
}
console.log(isPalin? 1 : 0);