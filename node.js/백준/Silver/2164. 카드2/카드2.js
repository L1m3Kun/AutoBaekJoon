const input = Number(require('fs').readFileSync('/dev/stdin').toString().trim());
let ans = 1;
while (input > ans){
    ans <<= 1;
}
console.log((input << 1) - ans);