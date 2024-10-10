function solution(board, moves) {
    const columns = board[0].map((_, colIndex) => board.map(row => row[colIndex]).reverse())
    const filteredColumns = columns.map(column => column.filter(doll => doll !== 0))
    const dollBucket = moves.map((command)=> filteredColumns[command-1].pop()).filter(item => item !== undefined)
    const [_,score] = dollBucket.reduce(
        ([crushedDolls,score], char)=> {
            if(crushedDolls.length > 0 && crushedDolls[crushedDolls.length -1] === char){
                crushedDolls.pop();
                score += 2;
            } else {
                crushedDolls.push(char)
            }
            return [crushedDolls, score]
        },
        [[], 0]
    )
    
  
    return score
    
}