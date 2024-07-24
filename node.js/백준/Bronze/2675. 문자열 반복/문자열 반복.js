const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const ans = [];

input.slice(1).forEach((e) => {
    const tmp = [];
    const [repeat, str] = e.split(' ');
    for (let i = 0; i < str.length; i++){
        for (let j= 0; j < Number(repeat); j++){
            tmp.push(str[i]);
        }
    }
    ans.push(tmp.join(''));
});
console.log(ans.join('\n'));