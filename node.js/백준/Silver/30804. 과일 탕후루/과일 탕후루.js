const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const N = Number(input[0]);
const fruits = input[1].split(' ').map(Number);
const count = { [fruits[0]]: 1};
let [i, j] = [0, 1];
let maxV = 1;
while (i <= j && j < N) {
    
    if (fruits[j] in count) {
        count[fruits[j++]] ++;
    } else {
        count[fruits[j++]] = 1;
    }
    
    while (Object.keys(count).length > 2) {
        count[fruits[i]] --;
        if (count[fruits[i]] === 0) {
            delete count[fruits[i]];
        }
        i ++;
    }
    maxV = Math.max(maxV, j-i);
}


console.log(maxV);