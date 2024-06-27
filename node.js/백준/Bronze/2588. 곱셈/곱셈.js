const fs = require('fs');
const [a, b] = fs.readFileSync(0, 'utf-8').toString().trim().split('\n').map(Number);

const result = [];
result.push((a*(b%10)));
result.push((a*(parseInt(b/10)%10)));
result.push((a*(parseInt(b/100))));
result.push(a*b);
console.log(result.join('\n'));