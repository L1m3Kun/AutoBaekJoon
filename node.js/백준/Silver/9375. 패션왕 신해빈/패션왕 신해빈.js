const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');
const ans = [];
let t = 1;
while (t < input.length){
    const N = Number(input[t]);
    const clothes = {};
    input.slice(t+1, t+1+N).forEach((e) => {
        const [name, label] = e.split(' ');
        if (label in clothes) {
            clothes[label] ++;
        } else {
            clothes[label] = 1;
        }
    });
    t+= 1+N;

    let branches = Object.values(clothes).reduce((prev, now) => prev*(now+1), 1)
    branches --;
    ans.push(branches);
}
console.log(ans.join('\n'));