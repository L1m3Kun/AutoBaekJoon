const fs = require('fs');
const [A, B, C] = fs.readFileSync('/dev/stdin')
                    .toString()
                    .trim()
                    .split('\n')
                    .map(Number);

const ans = Array(10).fill(0);
const result = (A*B*C).toString()
for (let s of result){
    ans[Number(s)] ++;
}
console.log(ans.join('\n'));