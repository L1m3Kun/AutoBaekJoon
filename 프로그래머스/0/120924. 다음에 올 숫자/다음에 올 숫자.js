function solution(common) {
    var answer = 0;
    for (let num_index=2; num_index < common.length;num_index++){
        let first = common[1] - common[0];
        let second = common[2] - common[1];
        if ( first === second ){
            return common[common.length-1] + first;
        }
        else{
            return common[common.length-1] * (second / first);
        };
    };
    return answer;
}