function solution(my_string) {
    let answer = 0;
    
    for(let char of my_string){
        console.log(char, Number(char))
        if (!isNaN(Number(char))) answer += Number(char);
    }
    
    return answer;
}