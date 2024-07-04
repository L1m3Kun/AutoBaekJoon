const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let ans = '';
const stack = [];
input.slice(1).forEach((e) => {
    const [order, num] = e.split(' ');
    switch(order) {
        case 'push':
            stack.push(num);
            break;
        case 'pop':
            ans += stack.length > 0 ? `${stack.pop()}\n` : '-1\n';
            break;
        case 'size':
            ans += `${stack.length}\n`;
            break;
        case 'empty':
            ans += stack.length > 0 ? '0\n' : '1\n';
            break;
        default:
            ans += stack.length > 0 ? `${stack[stack.length-1]}\n` : '-1\n';
            break;
    }
})
console.log(ans);


