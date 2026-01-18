const fs = require('fs');
const [[n], arr] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(e=>e.split(" ").map(Number));
const sa = arr.sort((a,b) => a-b);
let [i,j] = [0, n-1];
const ans = [i, j];
while (i < j) {
    const absSum = Math.abs(sa[i] + sa[j]);
    const standard = Math.abs(sa[ans[0]] + sa[ans[1]]);
    if (standard > absSum) {
        ans[0] = i;
        ans[1] = j;
    } 
    if (sa[i] === sa[j]) break;
    if (sa[i] + sa[j] > 0){
        j--;
    } else {
        i++;
    }
}
console.log(`${sa[ans[0]]} ${sa[ans[1]]}`);