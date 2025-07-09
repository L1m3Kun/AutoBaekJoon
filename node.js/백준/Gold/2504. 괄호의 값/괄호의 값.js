const input = require('fs').readFileSync('/dev/stdin').toString().trim();
const brackets = {
    '(':1,
    '[':2,
    ')':3,
    ']':4,
};
const stack = [];
let ans = 0;
Array.from(input).some((b)=>{
    if (brackets[b] <= 2) stack.push([brackets[b], 0]);
    else {
        if (stack.length < 1) {
            ans = 0;
            return true;
        }
        
        const [type, prefix] = stack.pop();
        if ((type & 1) !== (brackets[b] & 1)) {
            ans = 0;
            return true;
        }
        if (stack.length > 0) {
            const [_, num] = stack.pop();
            stack.push([_, num + (prefix ? prefix * (type & 1 ? 2 : 3) : type & 1 ? 2 : 3)]);
        } else {
            ans += prefix ? prefix * (type & 1 ? 2 : 3) : type & 1 ? 2 : 3;
        }
    }
    return false;
});

console.log(ans);