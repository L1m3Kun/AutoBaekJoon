const fs = require('fs');
const settings = () => {
    const input = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
    // const input = fs.readFileSync('input.txt').toString().split('\n');
    const N = Number(input[0]);
    const energy = [];
    input.slice(1,-1).forEach((e) => {
        energy.push([...e.split(' ').map(Number)]);
    })
    const K = Number(input[input.length-1]);
    return [N, energy, K];
}

const main = (N, energy, K) => {
    const dp = []
    for (let i = 0; i< N; i++){
        dp.push([100000, 100000]);
    }
    dp[0] = [0,0];
    for (let i = 0; i< N; i++) {
        if (N-1-i >= 1){
            dp[i+1][0] = Math.min(dp[i+1][0], dp[i][0]+energy[i][0]);
            dp[i+1][1] = Math.min(dp[i+1][1], dp[i][1]+energy[i][0]);
        }
        if (N-1-i >= 2){
            dp[i+2][0] = Math.min(dp[i+2][0], dp[i][0]+energy[i][1]);
            dp[i+2][1] = Math.min(dp[i+2][1], dp[i][1]+energy[i][1]);
        }
        if (N-1-i >= 3){
            dp[i+3][1] = Math.min(dp[i+3][1], dp[i][0]+K);
        }
    }

    console.log(Math.min(...dp[N-1]));
}

const [N, energy, K] = settings();
main(N, energy, K);