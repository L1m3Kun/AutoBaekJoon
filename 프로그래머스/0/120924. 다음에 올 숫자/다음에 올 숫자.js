function solution(common) {
    var answer = 0;
    const first = common[1] - common[0];
    const second = common[2] - common[1];
        
    if ( first === second ){
        return common[common.length-1] + first;
    }
    else{
        return common[common.length-1] * (second / first);
    };
    
    return answer;
}