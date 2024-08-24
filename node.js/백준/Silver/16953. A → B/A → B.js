const fs =require('fs');
let [A,B] = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split(' ')

let ans = -1;
let cnt = 1;
while (Number(A) <= Number(B)){
    if (A === B) {
        ans = cnt;
        break;
    }else if (B[B.length-1] === '1' && B.length>1){
        B = B.slice(0, B.length-1);
        cnt ++;
    } else if (Number(B) % 2 === 0) {
        B = (Number(B)>>1).toString();
        cnt ++;
    } else {
        break;
    }
    
}

console.log(ans);
