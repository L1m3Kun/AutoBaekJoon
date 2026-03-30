function solution(n) {
    let answer = 0;
    let [i,j] = [0,1];
    let sum = 1;
    while (i < j) {
        if (sum >= n) {
            if (sum === n) answer ++;
            i ++;
            sum -= i;
        } else {
            j ++;
            sum += j;
        } 
    }
    return answer;
}