const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const schedules = input.slice(1).map((e) => (e.split(' ').map(Number))).sort((a, b) => {
    if (a[1] > b[1]) {
        return 1;
    } else if(a[1] === b[1]){
        if (a[0] > b[0]) {
            return 1;
        } else {
            return -1;
        }
    } else {
        return -1;
    }
});

let ans = 0;
let end = 0;
schedules.forEach(([s,e]) => {
    if (s >= end) {
        ans ++;
        end = e;
    }
});

console.log(ans);