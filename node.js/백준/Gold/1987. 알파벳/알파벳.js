const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const [R, C] = input[0].split(' ').map(Number);
const alphabets = input.slice(1);

const visited = Array(26).fill(0);
visited[alphabets[0][0].charCodeAt()-65] = 1;
let maxV = 1;
const bt = (i,j,c) => {
    maxV = Math.max(maxV, c);
    for (let [ni, nj] of [[i+1,j], [i-1,j], [i,j-1], [i,j+1]]) {
        if (0 <= ni && ni < R && 0 <= nj && nj < C && !visited[alphabets[ni][nj].charCodeAt()-65]) {
            visited[alphabets[ni][nj].charCodeAt()-65] = 1;
            bt(ni,nj,c+1);
            visited[alphabets[ni][nj].charCodeAt()-65] = 0;
        }
    }
}
bt(0,0,1);
console.log(maxV);