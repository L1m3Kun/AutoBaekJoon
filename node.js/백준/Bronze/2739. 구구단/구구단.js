const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());
const ans = [];
for (let i = 1; i < 10; i++) {
    ans.push(`${n} * ${i} = ${n*i}`);
}
console.log(ans.join("\n"));