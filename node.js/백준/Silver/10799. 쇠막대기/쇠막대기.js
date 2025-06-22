const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const [_, answer] = Array.from(input).reduce(([stack, ans, isLaser], str) => {

    if (str === "("){
        stack ++;
        isLaser = 1;
    } else {
        if (isLaser) ans += stack - 1;
        else ans ++;
        stack --;
        isLaser = 0;
    }
    return [stack, ans, isLaser];
}, [0,0, 0]);
console.log(answer);