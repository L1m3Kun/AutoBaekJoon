const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const brackets = {
    "(" : 1,
    "[": 2,
    ")": 3,
    "]": 4,
};

const ans = input.reduce((ans, phrase) => {
    const stack = [];
    const isPerfect = Array.from(phrase.trim()).every((char) => {
        if (char in brackets){
            if (brackets[char] <= 2) {
                stack.push(brackets[char]);
            } else {
                if (stack.length < 1) return false;
                const cand = stack.pop();
                if ((cand & 1) !== (brackets[char] & 1)) return false;
            }
        }
        return true;
    });
    ans.push(isPerfect && stack.length < 1 ? "yes" : "no");
    return ans;
}, []);
console.log(ans.slice(0, ans.length - 1).join('\n'))