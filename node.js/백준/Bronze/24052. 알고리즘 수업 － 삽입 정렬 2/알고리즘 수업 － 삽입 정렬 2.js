const [[N, K],A] = require("fs").readFileSync("/dev/stdin")
                                .toString()
                                .trim()
                                .split("\n")
                                .map((line)=>line.split(" ").map(Number));
const insertionSort = (arr) => {
    let k = 0;
    for (let i = 1; i< N; i++){
        let newItem = arr[i];
        let loc = i-1;
        while(0<= loc && newItem < arr[loc]){
            arr[loc+1] = arr[loc];
            if (++k === K) return arr.join(" ");
            loc --;
        }
        if (loc + 1 !== i) {
            arr[loc+1] = newItem;
            if (++k === K) return arr.join(" ");
        }
    }
    return -1;
};

console.log(insertionSort(A));