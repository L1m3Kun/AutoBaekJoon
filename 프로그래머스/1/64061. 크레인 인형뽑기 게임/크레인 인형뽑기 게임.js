function solution(board, moves) {
    var answer = 0;
    const stack = [];
    const height = board.length, width = board[0].length;
    
    const setIdxArray = (w, h) => {
        const idxArray = Array(w).fill(h-1);
        for (let i = 0; i < w; i++) {
            for (let j = 0; j < h; j++) {
                if (board[j][i]) {
                    idxArray[i] = j;
                    break;
                }
            }
        }
        return idxArray;
    }
    
    const dollIdxArray = setIdxArray(width, height);
    // console.log(dollIdxArray)
    
    moves.forEach(e => {
        // console.log('dollidx', dollIdxArray);
        const w = e-1;
        const h = dollIdxArray[w];
        if (h < height) {
            const doll = board[h][w];
            if (stack.length > 0 && doll === stack[stack.length-1]){
                stack.pop();
                answer ++;
            } else {
                stack.push(doll);
            }
            dollIdxArray[w] ++;    
        } 
        // console.log('e', e);
        // console.log('stack', stack);
        // console.log('answer', answer);
        
    });
    return answer * 2;
}