const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const noHear = input.slice(1, N+1);
const noSee = new Set(input.slice(N+1));
const ans = [];

for(e of noHear) {
    if (noSee.has(e)){
        ans.push(e);
    }
}
ans.sort((a,b) => {
    if (a>b) return 1;
    else if (a===b) return 0;
    else return -1;
})
console.log(ans.length);
console.log(ans.join('\n'));