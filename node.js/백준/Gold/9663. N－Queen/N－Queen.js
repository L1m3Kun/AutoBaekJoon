const fs = require('fs');
const n = Number(
    fs.readFileSync('/dev/stdin')
    .toString()
    .trim()
);

const leftCross = Array(n<<1 - 1).fill(0);
const rightCross = Array(n<<1 - 1).fill(0);
const col = Array(n).fill(0);

let num = 0;
const bt = (s, e) => {
    if (s === e) {
        num ++;
        return;
    }
    
    for (let i = 0; i < e; i++){
        if (col[i] || leftCross[s+i] || rightCross[e-i+s-1]) continue;
        col[i] = 1;
        leftCross[s+i] = 1;
        rightCross[e-i+s-1] = 1;
        bt(s+1, e);
        col[i] = 0;
        leftCross[s+i] = 0;
        rightCross[e-i+s-1] = 0;
    }
    
}
    
bt(0, n);
console.log(num);
