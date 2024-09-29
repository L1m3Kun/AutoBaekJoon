const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const liquid = input[1].split(' ').map(BigInt).sort((a,b) => a >= b ? 1 : -1);
let [i, j] = [0,N-1];
let minv = 1_000_000_000_000_001n
let ans = [liquid[i], liquid[j]];

const abs = (num) => num >= 0n ? num : -num;

while (i < j) {
    const mid = liquid[i] + liquid[j];
    if (abs(mid) < abs(minv)){
        minv = mid;
        ans = [liquid[i], liquid[j]];
    }
    if (mid === 0n) {
        ans = [liquid[i], liquid[j]];
        break;
    } else if (mid < 0n)  {
        i ++;
    } else {
        j --;
    }
}
console.log(ans.join(' '));