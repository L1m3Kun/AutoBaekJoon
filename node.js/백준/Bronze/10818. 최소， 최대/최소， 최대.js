const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const sorted_arr = input[1].split(' ').map(Number).sort((a,b) => a-b);
console.log(sorted_arr[0], sorted_arr[Number(input[0])-1]);