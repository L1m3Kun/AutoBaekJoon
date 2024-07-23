const fs = require('fs');
const [start, end] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const primary = Array(10001).fill(1);
primary[0] = 0;
primary[1] = 0;

for (let i=2; i< 2501; i++){
    for (let j=i+i;j < 10001;j+=i){
        primary[j] = 0;
    }
}
let ans=[0,-1];
for (let i=start; i<end+1; i++){
    if (primary[i]){
        if (ans[1] === -1) {
            ans[1] = i
        }
        ans[0] += i
    }
}
if (ans[0] === 0) {
    console.log(-1)
} else {
    console.log(ans.join('\n'));    
}

