function solution(names) {
    const ans = [];
    for (let i = 0 ; i < names.length ; i += 5) {
        ans.push(names[i]);
    }
    return ans;
}