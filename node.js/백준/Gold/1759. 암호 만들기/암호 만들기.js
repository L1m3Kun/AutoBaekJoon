const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin')
                 .toString()
                 .trim()
                 .split("\n")
const [L, C] = inputs[0].split(" ").map(Number);
const arr = inputs[1].split(" ").sort();
const moem = new Set(['a', 'e', 'i', 'o', 'u']);
const ans = [];
const dfs = (idx, secret, hasMoem) => {

    if (secret.length === L) {

        return hasMoem && (L-hasMoem) >= 2 && ans.push(secret);
    }
    if (idx === C) return;

    if(moem.has(arr[idx])){
        dfs(idx+1, secret + arr[idx], hasMoem+1);             
    } else {
        dfs(idx+1, secret + arr[idx], hasMoem);             
    }

    dfs(idx + 1, secret, hasMoem);
}

dfs(0, "", 0);
console.log(ans.join('\n'));