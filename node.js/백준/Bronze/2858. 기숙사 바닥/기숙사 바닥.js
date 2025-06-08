const fs = require('fs');
const [r, b] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const square = r+b;
for (let i = 1; i <= Math.sqrt(square); i++) {
    if (square % i === 0){
        const [w, l] = [i, square/i];
        if (l+w === (r+4)/2){
            console.log(l, w);
            break;
        }
    }
}