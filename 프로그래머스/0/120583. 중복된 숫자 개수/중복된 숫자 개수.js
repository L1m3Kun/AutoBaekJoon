function solution(array, n) {
    
    return array.reduce((ans, now) => now === n ? ans + 1 : ans,0);
}