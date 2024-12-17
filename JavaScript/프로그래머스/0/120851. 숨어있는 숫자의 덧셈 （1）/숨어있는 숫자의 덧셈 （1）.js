// function solution(my_string) {
//     let answer = 0;
    
//     for(let char of my_string){
//         if (!isNaN(Number(char))) answer += Number(char);
//     }
    
//     return answer;
// }

const solution = (my_string) => Array.from(my_string).reduce((pre, now) => isNaN(Number(now)) ? pre : pre + Number(now),0);