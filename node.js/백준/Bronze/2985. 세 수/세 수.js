const fs = require('fs');
const [num1, num2, num3] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const operator = ['+', '*', '-', '/'];
const calculator = (a, b, op) =>{
    switch(op){
        case '+':
            return a+b;
        case '-':
            return a-b;
        case '*':
            return a*b;
        case '/':
            return a/b;
    }
    return a;
};
let ans;
const solution = (num1, num2, standard) => operator.some((oper) => {
    const calculatedNum = calculator(num1, num2, oper);
    if (calculatedNum === standard) {
        ans = oper
        return true;
    }
    return false;
});

if (solution(num1, num2, num3)){
    console.log(num1 + ans + num2 + '=' + num3);
} else {
    solution(num2, num3, num1);
    console.log(num1 + '=' + num2 + ans + num3);
}
