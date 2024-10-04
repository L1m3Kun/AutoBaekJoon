const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const ans = input.slice(1).map(e => e.split(' ').map(Number)).sort((a,b) => {
    if (a[0] < b[0]) return -1 ;
    else if (a[0] > b[0]) return 1; 
    else {
        if (a[1] < b[1]) return -1;
        else return 1;
    }
});
console.log(ans.map(e => e.join(' ')).join('\n'));