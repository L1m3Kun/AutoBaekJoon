// 9012 괄호
const fs = require("fs");

const settings = () => {
    // const input = fs.readFileSync("input.txt").toString().trim().split("\n");
    const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    return input.slice(1);
}


const main = (bracket) => {
    let stack = 0;
    let ans = "YES"
    for (let b of bracket) {
        if (b === "("){
            stack ++;
        } else {
            stack --;
        }
        // console.log(b, stack)
        if (stack < 0){
            ans = "NO";
            break;
        }
    }
    // console.log(stack.length);

    if (stack !== 0) {
        ans = "NO";
    }

    console.log(ans);
}

const brackets = settings();

for (let bracket of brackets) {
    main(bracket);
}

