const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const answer = input.slice(1).reduce((ans, par) => {
    let stack = 0;
    const isValid = Array.from(par).some((str) => {
       if (str === "(") {
           stack ++;
       } else {
           if (stack) {
               stack --;
           } else return true;
       }
       return false;
    });
    ans.push(isValid?"NO": stack ? "NO": "YES");
    return ans;
},[]);
console.log(answer.join('\n'));