// function solution(numbers, n) {
//     let answer = 0;
//     for (num of numbers){
//         if (answer > n) break;
//         answer += num;
//     }
//     return answer
// }

function solution(numbers, n) {
    const sum = numbers.reduce((prev, num) => (prev <= n ? prev+num : prev), 0)
    return sum
}