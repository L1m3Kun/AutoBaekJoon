const fs = require("fs");
const [[N, K], A] = fs.readFileSync("/dev/stdin")
                      .toString()
                      .trim()
                      .split("\n")
                      .map((line)=>line.split(" ").map(Number));

const selectionSort = (arr) => {
    let k = 0;
    for (let last = N-1; last > 0; last --){
        let maxIdx = 0;
        for (let i = 0; i <= last; i++){
            if (arr[i] > arr[maxIdx]) maxIdx = i;
        }
        
        if (maxIdx !== last){
            [arr[maxIdx], arr[last]] = [arr[last], arr[maxIdx]];
            k++;
            if (k === K) return arr.join(" ");
        }
    }
    return -1;
}

console.log(selectionSort(A));