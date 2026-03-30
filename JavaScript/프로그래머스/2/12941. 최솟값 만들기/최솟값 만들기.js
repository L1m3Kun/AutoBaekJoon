function solution(A,B){
    const n = A.length;
    
    A.sort((a,b) => a-b);
    B.sort((a,b) => b-a);
    
    let ans = 0;
    return A.reduce((prev, acc, idx)=>{
        return prev + acc * B[idx];
    }, 0);
}