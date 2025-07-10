const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const answer = input.slice(1).reduce(([ans, stack], condition) => {
    const [order, element] = condition.split(' ');
    switch(order) {
        case "push":
            stack.push(Number(element));
            break;
        case "pop":
            ans.push(stack.pop() || -1);
            break;
        case "size":
            ans.push(stack.length);
            break;
        case "empty":
            ans.push(!stack.length ? 1:0);
            break;
        case "top":
            ans.push(stack[stack.length-1] || -1);
            break;
    }
    return [ans, stack];
}, [[], []]);

console.log(answer[0].join('\n'));