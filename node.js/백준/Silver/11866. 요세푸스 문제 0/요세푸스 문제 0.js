const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const answerForm = (arr) => `<${arr.join(', ')}>`;

const que = Array.from({length: N}, (_, i) => i+1);
let head = 0;
let cnt = 0;
const ans = [];
while (que.length > head) {
    cnt ++;
    if (cnt % K) {
        que.push(que[head++]);
    } else {
        ans.push(que[head++]);
    }
}
console.log(answerForm(ans));
