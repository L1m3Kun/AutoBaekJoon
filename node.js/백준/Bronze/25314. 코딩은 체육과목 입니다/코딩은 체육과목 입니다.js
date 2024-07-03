const fs =require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());
let ans = '';

for (let i=0;i < parseInt(N/4); i++){
    ans += 'long ';
}
console.log(ans+'int');