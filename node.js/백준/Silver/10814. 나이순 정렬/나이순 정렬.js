const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const arr = input.slice(1).map(e => e.split(' ')).sort((a,b) => {
    if (Number(a[0]) < Number(b[0])){
        return -1;
    } else if (Number(a[0]) === Number(b[0])){
        return b[1] -a[1];
    } else {
        return 1;
    }
})
const ans = arr.map(e => e.join(' '));
console.log(ans.join('\n'));