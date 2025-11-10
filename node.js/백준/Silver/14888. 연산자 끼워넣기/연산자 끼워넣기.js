const fs = require('fs');
const inputs = fs.readFileSync("/dev/stdin")
                 .toString()
                 .trim()
                 .split('\n');

const n = Number(inputs[0]);
const arr = inputs[1].split(' ').map(Number);
const operCount = inputs[2].split(' ').map(Number);
const operator = ['+', '-', '*', '/'];
const operators = operCount.reduce((oper, c, idx)=>{
    for (let i = 0; i<c;i++){
        oper.push(operator[idx]);
    }
    return oper;
}, []);

const calculate = (str) => {
    const a =  str.split("").reduce((acc, cur, idx)=>{
        switch(cur){
            case '-':
                acc -= arr[idx+1];
                break;
            case '*':
                acc *= arr[idx+1];
                break;
            case '/':
                const cand = acc / arr[idx+1];
                if (Object.is(acc,-0)) acc =  0;
                else if (acc < 0) acc = Math.ceil(cand);
                else acc = Math.floor(cand);
                break;
            default:
                 acc += arr[idx+1];
                break;
        }
        return Object.is(acc, -0) ? 0 : acc;
    }, arr[0]);
    return a;
};

let [minV, maxV] = [10**10,-(10**10)];
const visited = Array(n-1).fill(0);
const dfs = (str) => {
    if (str.length === n-1){
        const c = calculate(str);
        minV = Math.min(minV, c);
        maxV = Math.max(maxV, c);
        return;
    }

    for (let j = 0; j < n-1; j++){
        if (visited[j]) continue;
        visited[j] = 1;
        dfs(str+operators[j]);
        visited[j] = 0;
    }
};

dfs('');
console.log(maxV);
console.log(minV);