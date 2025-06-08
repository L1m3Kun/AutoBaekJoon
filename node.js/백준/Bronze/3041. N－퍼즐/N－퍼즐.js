const fs = require('fs');
const square = fs.readFileSync('/dev/stdin').toString().split('\n');
const manhattanDistance = (y, x, i, j) => Math.abs(y-i) + Math.abs(x-j); 
const ans = square.reduce((acc, str, i)=>{
    let tmp = acc;

    Array.from(str).forEach((char, j)=>{
        const [originIndexNum, currentIndexNum] = [char.charCodeAt(0) - 65, i*4+j];
        if (char !== '.' && originIndexNum !== currentIndexNum){
            const originJ = originIndexNum % 4;
            const originI = (originIndexNum - originJ) / 4;
            tmp += manhattanDistance(i, j, originI, originJ);
//            console.log(`current Num: ${currentIndexNum}, origin Num: ${originIndexNum}, currI: ${i}, currJ: ${j}, originI: ${originI}, originJ: ${originJ}`)
        }
    });
    return tmp;
}, 0);
console.log(ans);