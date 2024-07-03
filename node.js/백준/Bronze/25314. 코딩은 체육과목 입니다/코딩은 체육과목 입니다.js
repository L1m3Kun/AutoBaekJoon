const fs =require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());
const ans = [];

for (let i=0;i < parseInt(N/4); i++){
    ans.push('long');
}
ans.push('int');
console.log(ans.join(' '));