// 요구사항: start_num에서 end_num까지 배열에 1씩 감소하여 담는다.
// function solution(start_num, end_num) {
//     const answer = [];
//     for(let num = start_num; num >= end_num; num-=1){
//         answer.push(num);
//     }
//     return answer;
// }

function solution(start_num, end_num) {
    return Array.from({length: start_num - end_num +1}, (_,i) => start_num-i);
}