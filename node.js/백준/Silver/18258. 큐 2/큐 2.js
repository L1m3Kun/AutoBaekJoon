const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');
const que = {};
let [head, rear] = [0,0];
const ans = [];
input.slice(1).forEach((e) => {
    const order = e.split(' ');
    switch(order[0]){
        case 'push':
            que[rear++] = Number(order[1]);
            break;
        case 'pop':
            
            if (head<rear){
                ans.push(que[head]);
                delete que[head++];
            } else {
                ans.push(-1);
            }
            break;
        case 'size':
            ans.push(rear-head);
            break;
        case 'empty':
            ans.push(head < rear ? 0 : 1);
            break;
        case 'front':
            ans.push(head < rear ? que[head] : -1);
            break;
        case 'back':
            ans.push(head < rear ? que[rear-1] : -1);
            break;
        default:
            break;
    };
});
console.log(ans.join('\n'));
