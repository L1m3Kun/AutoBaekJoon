const fs = require('fs');
const [n, m] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const primary = Array(m+1).fill(1);

primary[0] = 0;
primary[1] = 0;
for (let i=2; i<=Math.sqrt(m); i++){
    for (let j=i+i; j<= m; j+=i){
        primary[j] = 0;
    }
}
const ans = [];
for (let i=n; i<m+1; i++) {
    if (primary[i]) ans.push(i);
}

console.log(ans.join('\n'));