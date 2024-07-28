const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ');
const chessField = input.slice(1);
const check = (sI, sJ) => {
    // 짝수, 홀수
    const offset = 'WBWBWBWB'; 
    const changes = [0,0];
    for (let i=sI; i<sI+8;i++){
        for (let j=sJ; j<sJ+8;j++){
            if (offset[j-sJ] === chessField[i][j]){
                if (i % 2){
                    changes[0] ++;    
                } else {
                    changes[1] ++;    
                }
            } else {
                if (i % 2){
                    changes[1] ++;    
                } else {
                    changes[0] ++;    
                }                
            }       
        }
    }
    return Math.min(...changes);
}

let minV = 2500;
for (let i=0;i<=N-8;i++){
    for (let j=0;j<=M-8;j++){
        minV = Math.min(check(i,j), minV);
    }
}
console.log(minV);