const bin = (num) => Array.from(num.toString(2));

function solution(s) {
    const ans = [0,0];
    let str = Array.from(s);
    while (str.length > 1){
        const tmp = str.filter(char => char === '1');
        
        ans[1] += str.length - tmp.length;
        ans[0] ++;
        
        str = bin(tmp.length);
    }
    
    return ans;
}