function solution(n) {
    let ans = 0;
    for (let i=1; i<= n;i++){
        if (!(n % i)) ans += i;
    }
    return ans;
}