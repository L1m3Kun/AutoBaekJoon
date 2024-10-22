const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(e => e.split(' ').map(Number));
const [N,M] = input[0];
const arr = Array.from({length: N}, (_,i) => i+1);

input.slice(1).forEach(([s,e]) => {
    arr.slice(s-1, e).reverse().forEach((num,i) => {
        arr[s-1+i] = num;
    })    
});

console.log(arr.join(' '));