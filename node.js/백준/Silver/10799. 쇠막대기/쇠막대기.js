const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const [_, answer] = Array.from(input).reduce(([stack, ans], str, idx) => {
    if (str === "("){
        stack ++;
    } else {
        stack --;
        if (input[idx-1]==="(") ans += stack;
        else ans ++;
    }
    return [stack, ans];
}, [0,0]);
console.log(answer);