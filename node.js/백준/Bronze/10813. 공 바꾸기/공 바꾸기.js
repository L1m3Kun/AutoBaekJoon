const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, _] = input[0].split(' ').map(Number);
const basket = Array(N+1).fill(0).map((_,i) => i);
input.slice(1).forEach(ball => {
    const [s, e] = ball.split(' ').map(Number);
    if (s !== e) {
        [basket[s], basket[e]] = [basket[e], basket[s]];
    }
});
console.log(basket.slice(1).join(' '));