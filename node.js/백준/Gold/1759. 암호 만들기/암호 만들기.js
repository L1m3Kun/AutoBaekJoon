const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin')
                 .toString()
                 .trim()
                 .split("\n")
const [L, C] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split(" ").sort();
const moem = new Set(['a', 'e', 'i', 'o', 'u']);
const lastIndexOfMoem = arr.reduce((i ,a, idx)=>moem.has(a) ? idx : i, 0);
const ans = [];
const dfs = (idx, secret, hasMoem) => {
    if (secret.length === L) return hasMoem && (L-hasMoem) > 1 && ans.push(secret);
    if (idx === C || (C - idx + secret.length) < L) return;
    if (moem.has(arr[idx])) dfs(idx+1, secret + arr[idx], hasMoem+1); 
    else {
        if (!hasMoem && lastIndexOfMoem < idx) return;
        dfs(idx+1, secret + arr[idx], hasMoem); 
    }
    dfs(idx + 1, secret, hasMoem);
}

dfs(0, "", 0);
console.log(ans.join('\n'));