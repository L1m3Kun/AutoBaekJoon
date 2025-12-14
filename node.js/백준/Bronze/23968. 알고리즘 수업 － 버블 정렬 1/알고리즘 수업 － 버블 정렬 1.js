const fs = require("fs");
const [[N, K], A] = fs.readFileSync("/dev/stdin")
                      .toString()
                      .trim()
                      .split("\n")
                      .map((line)=>line.split(" ").map(Number));

const bubbleSort = (arr) => {
    let k = 0;
    for (let last = N-1; last > 0; last --){
        for (let i = 0; i < last; i++){
            if (arr[i] > arr[i+1]) {
                k ++;
                if (k === K) return [arr[i+1], arr[i]].join(" ");
                [arr[i], arr[i+1]] = [arr[i+1], arr[i]];
            }
        }
    }
    return -1;
};

console.log(bubbleSort(A));