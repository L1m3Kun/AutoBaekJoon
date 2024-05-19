// 2143 두 배열의 합
const fs = require("fs");

const settings = () => {
    // const input = fs.readFileSync('input.txt').toString().split("\n");
    const input = fs.readFileSync('/dev/stdin').toString().split("\n");
    const T = Number(input[0]);
    const n = Number(input[1]);
    const A = input[2].split(" ").map(Number);
    const m = Number(input[3]);
    const B = input[4].split(" ").map(Number);
    return [T, n, A, m, B];
}


const main = (T) => (n, A) => (m, B) => {
    const candB = {};
    let prefix;
    let cnt = 0;
    for (let i =0;i < m; i++){
        prefix = 0;
        for (let j =i; j< m; j++){
            prefix += B[j];
            if(prefix in candB){
                candB[prefix] ++;
            }else{
                candB[prefix] = 1;
            }
        }
    }   
    
    for (let i =0;i < n; i++){
    prefix = 0;
        for (let j =i; j< n; j++){
            prefix += A[j];
            if ((T - prefix) in candB){
                cnt += candB[T-prefix];
            }
        }
    }
    
    console.log(cnt);
}

const [T, n, A, m, B] = settings();
main(T)(n, A)(m, B);