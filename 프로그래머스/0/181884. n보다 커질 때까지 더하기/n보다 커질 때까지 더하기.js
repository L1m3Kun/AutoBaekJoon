function solution(numbers, n) {
    let answer = 0;
    for (num of numbers){
        if (answer > n) break;
        answer += num;
    }
    return answer
}