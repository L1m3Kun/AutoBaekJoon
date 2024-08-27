const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');
const N = Number(input[0]);
const house = input.slice(1)
                   .map(e => e.split(' ').map(Number));
const dpRGB = Array.from(Array(N), () => new Array(3).fill(0));

for (let i = 0; i<3 ; i ++) { 
    dpRGB[0][i] = house[0][i];
}

for (let i = 1; i< N ; i ++) {
    for (let j = 0; j < 3 ; j ++ ) {
        dpRGB[i][j] = house[i][j] + Math.min(dpRGB[i-1][(j+1)%3], dpRGB[i-1][(j+2)%3]);
    }
}

console.log(Math.min(...dpRGB[N-1]));