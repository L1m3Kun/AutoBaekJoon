const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const ans = inputs.slice(1).map((password)=>{
    const [prefix, postfix] = Array.from(password).reduce(([prefix, postfix], char)=> {
            switch(char) {
                case "<":
                    if (prefix.length < 1) break;
                    postfix.push(prefix.pop());
                    break;
                case ">":
                    if (postfix.length < 1) break;
                    prefix.push(postfix.pop());
                    break;
                case "-":
                    if (prefix.length < 1) break;
                    prefix.pop();
                    break;
                default:
                    prefix.push(char);
                    break;
            }
            return [prefix, postfix];
        },[[], []]);

    return prefix.join('') + postfix.reverse().join('');
});
console.log(ans.join('\n'));