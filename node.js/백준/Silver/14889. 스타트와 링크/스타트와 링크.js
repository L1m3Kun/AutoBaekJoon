const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin')
                 .toString()
                 .trim()
                 .split('\n');
const n = Number(inputs[0]);
const table = inputs.slice(1)
                    .map((row) => row.split(" ").map(Number));
const all = Array.from({length: n}, (_, i) => i);
const calculateScore = (m) => {
    const enermy = all.filter((e) => !m.has(e));
    const members = Array(...m);
    let [mScore, eScore] = [0, 0];
    for (let i = 0; i < n; i ++) {
        if (m.has(i)){
            for (let j=0; j<(n>>1) ; j++){
                if (i !== members[j]){
                    mScore += table[i][members[j]];
                }
            }
        } else {
            for (let j=0; j<(n>>1) ; j++){
                if (i !== enermy[j]){
                    eScore += table[i][enermy[j]];
                }
            }
        }
    }
    return Math.abs(mScore-eScore);
}
const solution = () => {
    const stack = [[0, new Set([0])]];
    let minV = 10000;
    while(stack.length > 0) {
        const [node, visited] = stack.pop();
        if (visited.size === (n >> 1)) {
            minV = Math.min(minV, calculateScore(visited));
            continue;
        }
        for(let i = node+1; i< n; i++){
            if (!visited.has(i)){
                const newNode = new Set([...visited, i]);
                stack.push([i, newNode]);
            }
        }
    }
    return minV;
}

const answer = solution();
console.log(answer);