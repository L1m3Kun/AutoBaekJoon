const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, M] = input[0].split(" ").map(Number);
const matrix = input.slice(1, N+1).map((e) => e.split(" ").map(Number));
const testCase = input.slice(N+2, -1).map((e)=> e.split(" ").map(Number));
const answer = [];

const solution = (matrix, i, j, x, y) => {
    let answer = 0;
    for(let r = i; r < x; r++){
        for (let c = j; c < y ; c++) {
            answer += matrix[r][c];
        }
    }
    return answer;
}

testCase.forEach(([i, j, x, y]) => {
    answer.push(solution(matrix, i-1, j-1, x, y));
});
console.log(answer.join("\n"));