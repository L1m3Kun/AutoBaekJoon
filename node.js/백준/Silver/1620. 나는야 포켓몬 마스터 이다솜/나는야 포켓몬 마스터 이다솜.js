const fs= require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const nums = {};
const str = {};

input.slice(1, N+1).forEach((e, i)=> {
    nums[i+1] = e;
    str[e] = i+1;
});

const ans = [];
input.slice(N+1).forEach((e)=> {
    if (isNaN(e)) {
        ans.push(str[e]);
    } else {
        ans.push(nums[Number(e)]);
    }
});
console.log(ans.join('\n'));