function solution(rny_string) {
    let ans = '';
    for (let char of rny_string){
        if (char === 'm') ans += 'rn';
        else ans += char;
    }
    return ans;
}