const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let ans = '';
const que = {}
let [front, rear] = [-1, -1];

input.slice(1).forEach((e) => {
    const [order, num] = e.split(' ');
    switch(order) {
        case 'push':
            que[++rear] = num;
            break;
        case 'pop':
            if (front === rear) {
                ans += '-1\n';
            } else{
                ans += `${que[++front]}\n`;
            }
            break;
        case 'size':
            ans += `${rear-front}\n`;
            break;
        case 'empty':
            ans += front === rear ? '1\n' : '0\n';
            break;
        case 'front':
            ans += front === rear ? '-1\n': `${que[front+1]}\n`;
            break;
        default:
            ans += front === rear ? '-1\n': `${que[rear]}\n`;
    }
});
console.log(ans);
