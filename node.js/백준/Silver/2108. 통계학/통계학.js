const fs = require('fs');
const [N, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
arr.sort((a,b) => a-b);
const count = {};
arr.forEach((e)=>{
    if (e in count){
        count[e]++;
    } else {
        count[e] = 1;
    }
});
let total = 0;
let maxIdx = [];
for(let k in count) {
    total += count[k]*k;
    if (maxIdx.length===0){
      maxIdx.push(k);  
    } else if (count[maxIdx[0]] < count[k]){
        maxIdx = [k];
    } else if (count[maxIdx[0]] === count[k]){
        maxIdx.push(k);
    }
}
maxIdx.sort((a,b) => a-b);
const ans = [Math.round(total/N),arr[Math.floor(N/2)],maxIdx.length===1?maxIdx[0]:maxIdx[1],arr[N-1] - arr[0]];
console.log(ans.join('\n'));

