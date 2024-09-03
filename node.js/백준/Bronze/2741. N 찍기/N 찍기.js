const N = Number(require('fs').readFileSync('/dev/stdin').toString().trim());
const ans = [];
for (let i = 1; i <= N ; i++) {
    ans.push(i);
}
console.log(ans.join('\n'));