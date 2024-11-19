const boom = (arr, i, j) => {
    for (let y = i-1; y <= i+1; y++) {
        for (let x = j -1; x <= j+1; x++){
            if (0 <= y && y < arr.length && 0<= x && x < arr.length){
                arr[y][x] = 1;
            }
        }
    }
};

function solution(board) {
    const visited = Array.from({length: board.length}, () => Array(board.lenght).fill(0));
    for (let i = 0; i < board.length; i ++){
        for (let j = 0; j<board.length; j++) {
            if (board[i][j] === 1) {
                visited[i][j] = 1;
                boom(visited, i, j);
            }
        }
    }
    
    return visited.reduce((prev, now) => {
        return prev - now.reduce((cnt, b) => {
            if (b) cnt ++;
            return cnt;
        }, 0);
    }, board.length ** 2);
}