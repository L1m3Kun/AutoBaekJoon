const [str, _, ...orders] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const prefix = Array.from(str);
const postfix = orders.reduce((postfix, order) => {
    switch (order[0]){
        case "L":
            if (prefix.length < 1) break;
            postfix.push(prefix.pop());
            break;
        case "D":
            if (postfix.length < 1) break;
            prefix.push(postfix.pop());
            break;
        case "B":
            if (prefix.length < 1) break;
            prefix.pop();
            break;
        default:
            prefix.push(order[2]);
    }
    return postfix;
}, []);
console.log(prefix.join("") + postfix.reverse().join(""));