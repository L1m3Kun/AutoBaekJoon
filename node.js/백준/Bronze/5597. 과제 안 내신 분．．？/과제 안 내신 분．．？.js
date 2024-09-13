const fs =require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const attendance = new Set(Array.from({length: 30}, (_, i) => i+1));

input.forEach((e) => attendance.delete(e));

const ans = [...attendance].sort((a,b) => a-b);
console.log(ans.join('\n'));
