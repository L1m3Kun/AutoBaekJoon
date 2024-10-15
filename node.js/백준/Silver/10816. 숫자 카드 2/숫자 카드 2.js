const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const cntArr = new Map();
input[1].split(' ').forEach(e => {
    if (cntArr.has(e)){
        cntArr.set(e, cntArr.get(e)+1);
    } else {
        cntArr.set(e, 1);
    }
});
const ans = [];
input[3].split(' ').forEach(e => {
    if (cntArr.has(e)){
        ans.push(cntArr.get(e));
    } else {
        ans.push(0);
    }
});
console.log(ans.join(' '));