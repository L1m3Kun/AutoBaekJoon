const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');


const ans = input.slice(1).map((e) => {
    let [start, end, total] = [0,0,0];
    while (end < e.length) {
        if (e[end] === 'O'){
            total += end-start+1;
        }else {
            start = end+1;
        }
        end ++;
    }
    return total;
});

console.log(ans.join('\n'));