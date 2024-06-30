const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim());

let result = '';
for (let i = 1; i <= input; i++) {
    for (let j = 1; j <= i; j ++) {
        result += '*';
    }
    result += '\n';
}

console.log(result);