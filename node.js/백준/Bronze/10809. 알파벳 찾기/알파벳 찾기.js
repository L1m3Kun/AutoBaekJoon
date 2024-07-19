const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const alpha = Array(26).fill(-1);

[...input].forEach((e, i) => {
    const idx = e.charCodeAt() - 97;
    if (alpha[idx] === -1) {
        alpha[idx] = i;
    }
});

console.log(alpha.join(' '))