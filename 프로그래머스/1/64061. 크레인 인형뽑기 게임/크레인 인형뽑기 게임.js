const setIdxArray = (w, h, board) => {
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

function solution(board, moves) {
    
    const stack = [];
    const height = board.length, width = board[0].length;
    
    const dollIdxArray = setIdxArray(width, height, board);
    
    // moves.forEach(e => {
    //     const w = e-1;
    //     const h = dollIdxArray[w];
    //     if (h < height) {
    //         const doll = board[h][w];
    //         if (stack.length > 0 && doll === stack[stack.length-1]){
    //             stack.pop();
    //             answer ++;
    //         } else {
    //             stack.push(doll);
    //         }
    //         dollIdxArray[w] ++;    
    //     } 
    // });
    const [_, answer] = moves.reduce(([stack, score], move) => {
        const w = move - 1;
        const h = dollIdxArray[w];
        if (h < height) {
            const doll = board[h][w];   // 인형 위치로 인형 값 가져옴
            if (stack.length > 0&& doll === stack[stack.length -1]) {
                stack.pop();
                score += 2;
            } else {
                stack.push(doll);
            }
            dollIdxArray[w] ++; // 최상위 인덱스를 증가하므로써 현재 최상위 인형을 제외하고 실행
        }
        return [stack, score]
    }, [[], 0]);
    return answer;
}