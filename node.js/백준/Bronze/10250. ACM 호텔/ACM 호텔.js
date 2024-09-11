const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const ans = [];
input.slice(1).forEach((e) => {
    const [H, W, N] = e.split(' ').map(Number);
    if (N % H){
        ans.push(Math.ceil(N/H) < 10 ? `${N%H}0${Math.ceil(N/H)}` : `${N%H}${Math.ceil(N/H)}`)
    } else {
        ans.push(Math.ceil(N/H) < 10 ? `${H}0${Math.ceil(N/H)}` : `${H}${Math.ceil(N/H)}`)
    }
});
console.log(ans.join('\n'));