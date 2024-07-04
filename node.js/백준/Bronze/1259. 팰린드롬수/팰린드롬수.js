const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let ans = '';

const isPalindrom = (n, mid,e) => {
    for (let i=0; i <= mid; i++){
        if (e[i] !== e[n-i-1]){
            return 'no\n';
        }
    }
    return 'yes\n';
}

input.slice(0, -1).forEach((e) => {
    const n = e.length;
    const mid = parseInt(n / 2);
    ans += isPalindrom(n, mid,e);
});
console.log(ans);