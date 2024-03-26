function solution(s) {
    var answer = '';
    answer += s[0].toUpperCase();
    for (let index = 1; index < s.length; index ++){
        if (s[index-1] === " ") answer += s[index].toUpperCase();
        else answer += s[index].toLowerCase();
    };
    return answer;
}