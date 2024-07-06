const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input[1].split(' ').map(Number);
const v = Number(input[2]);

const counts = {};
arr.forEach((e) => {
    if (counts.hasOwnProperty(e)){
        counts[e] ++;
    } else {
        counts[e] = 1;
    }
});
if (counts.hasOwnProperty(v)){
    console.log(counts[v]);    
} else {
    console.log(0);
}
