const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin")
                 .toString()
                 .trim()
                 .split("\n");
const [N, S] = inputs[0].split(" ")
                        .map(Number);
const arr = inputs[1].split(" ")
                     .map(Number)
                     .sort((a,b) => a-b);
let ans = 0;
for (let i = 1; i < (1<<N); i++){
    let total = 0;
    for (let j = 0; j < N; j++){
        if (i & (1 << j)) {
            total += arr[j];
        }
    }
    if (total === S) ans ++;
}

console.log(ans);