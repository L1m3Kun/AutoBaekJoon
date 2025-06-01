const change = (num, radix) => {
    let ans = 0;
    while (num) {
        ans += num % radix;
        num /= radix;
        num = parseInt(num);
    }
    return ans;
}

const candidate = Array.from({length: 9000}, (_,i) => i+1000);

const answer = candidate.reduce((ans, num)=>{
    const check = change(num,10);
    const isSame = [12, 16].every((c) => change(num,c) === check);
    if (isSame) {
        ans.push(num);
    }
    return ans;
}, []);

console.log(answer.join('\n'));