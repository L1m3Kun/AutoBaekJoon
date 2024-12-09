function solution(n, numlist) {
    
    return numlist.reduce((ans, now) => {
        if(!(now % n)) ans.push(now);
        return ans;
    }, [] );
}