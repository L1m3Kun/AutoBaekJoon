function solution(s) {
    var answer = '';
    let nums = s.split(" ").map(Number);
    
    answer += Math.min.apply(null,nums);
    answer += " ";
    answer += Math.max.apply(null,nums);
    return answer;
}