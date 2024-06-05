// 1049 기타줄
const fs = require("fs");

const settings = () => {
    // const input = fs.readFileSync("input.txt").toString().trim().split("\n");
    const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    const [N] = input[0].split(" ").map(Number);
    let minSix = 10001;
    let minOne = 10001;
    input.slice(1).forEach((e) => {
        const [six, one] = e.split(" ").map(Number);
        minSix = Math.min(minSix, six);
        minOne = Math.min(minOne, one);
    })

    return [N, minSix, minOne];
}


const main = (N, minSix, minOne) => {
    
    if (minOne * 6 <= minSix) {
        console.log(minOne * N);
        return;
    } 
    
    let cost = 0;
    while (N >= 6) {
        cost += minSix;
        N -= 6;
    }
    
    if (N*minOne < minSix) {
        console.log(cost+N*minOne);
    } else{
        console.log(cost+minSix);
    }
}

const [N, minSix, minOne] = settings();
main(N, minSix, minOne);