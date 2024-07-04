const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());
let ans = '';

for (let i=1; i <= N; i++){
    for (let j =0; j < N-i ; j++){
        ans += ' ';
    }
    for (let j=0; j < i; j++) {
        ans += '*';
    }
    ans += '\n';
}
console.log(ans);