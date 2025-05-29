const fs= require('fs');
const [_, ...cases] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const dp = Array(100).fill(1);
for(let i = 2;i <= 100; i++){
  for(let j = i;j<=100;j+=i){
    dp[j-1] ++;
  }
}

const ans = cases.map((t) => dp.slice(0, t).reduce((openCount, roomNum) => openCount + (roomNum & 1), 0));
console.log(ans.join('\n'));