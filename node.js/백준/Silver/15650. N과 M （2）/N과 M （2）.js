const fs = require('fs');
const [n,m] = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split(" ")
                .map(Number);
const str = [];
const visited = Array.from({length: n+1}, ()=>0);
const ans = [];
const bt = (start) => {
    if (str.length === m) {
        ans.push(str.join(" "));
        return;
    }
    for (let i = start+1; i <= n; i++){
        if (visited[i]) continue;
        visited[i] = 1;
        str.push(i);
        bt(i);
        str.pop(i);
        visited[i] = 0;
    }
}

for (let i = 1; i <= n; i++){
    visited[i] = 1;
    str.push(i);
    bt(i);
    str.pop(i);
}
console.log(ans.join("\n"));