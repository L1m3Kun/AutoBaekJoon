const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const arr = input[1].split(' ').map(Number);

const primary = Array(1001).fill(1);
primary[0] = 0;
primary[1] = 0;

for (let i=2; i< 501; i++){
    for (let j=i+i;j < 1001;j+=i){
        primary[j] = 0;
    }
}
let ans=0;
arr.forEach((e) => {
    if (primary[e]) ans ++;
})

console.log(ans);