function solution(money) {
    const ans = [0,0];
    
    for (money;money>=5500;money-= 5500){
        ans[0]++;
    }
    ans[1] = money;
    return ans;
}