const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split(' ')
                .map(Number);
let ans = 'mixed';

if (input[0] === 1) {
    ans = 'ascending';
    for (let i=1; i<8;i++) {
        if (input[i] - input[i-1] !== 1){
            ans = 'mixed';
            break;
        }
    }
} else if(input[0] === 8) {
    ans = 'descending';
    for (let i=1; i<8;i++) {
        if (input[i-1] - input[i] !== 1){
            ans = 'mixed';
            break;
        }
    }
}
console.log(ans);