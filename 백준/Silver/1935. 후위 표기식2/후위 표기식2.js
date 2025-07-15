const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const postfix = inputs[1];
const keys = inputs.slice(2).reduce((obj, value, idx)=>{
    obj[String.fromCharCode(idx+65)] = Number(value);
    return obj;
},{});
const operator = new Set(["+","-","*","/"]);

const calculate = (oper, num1, num2) => {
    switch(oper){
        case "+":
            return num1 + num2;
        case "-":
            return num1 - num2;
        case "*":
            return num1 * num2;
        case "/":
            return num1 / num2;
    }
    return num1;
};

const stack = Array.from(postfix).reduce((stack, char) => {
    if (operator.has(char)){
        const num2 = stack.pop();
        const num1 = stack.pop();
        const acc = calculate(char, num1, num2);
        stack.push(acc);
    } else {
        stack.push(keys[char]);
    }
    return stack
}, []);
console.log(stack[0].toFixed(2));

