const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, q] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
const prefix = (s, e) => arr.slice(s, e).reduce((acc, num) => acc+ num, 0);
const ans = input.slice(2).map((query) => {
    const [order, ...rest] = query.split(' ').map(Number);
    switch(order){
        case 1:
            const re = prefix(rest[0]-1, rest[1]);
            [arr[rest[0]-1], arr[rest[1] -1]] = [arr[rest[1]-1], arr[rest[0] -1]];
            return re;
        case 2:
            return prefix(rest[0]-1, rest[1]) - prefix(rest[2]-1, rest[3]);
    }
});
console.log(ans.join('\n'));