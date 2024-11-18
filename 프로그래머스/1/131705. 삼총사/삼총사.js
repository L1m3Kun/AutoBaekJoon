function solution(number) {
    number.sort((a,b) => a-b);
    console.log(number)
    let ans = 0;
    
    for (let idx=0 ; idx < number.length; idx++) {
        if (number[idx] > 0) break;
        for (let i = idx+1; i< number.length; i++) {
            const mid = number[idx] + number[i];
            if (mid > 0) break;
            for (let j = i+1; j < number.length; j++){
                if (mid + number[j] === 0) {
                    console.log(idx, i, j)
                    ans ++;
                }
                else if (mid + number[j] > 0) break;
            }
        }
    }
    return ans;
}