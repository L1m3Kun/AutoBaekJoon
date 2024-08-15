const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [N, K] = input[0].split(' ').map(Number);
const coins = input.slice(1).map(Number).reverse();

let ans = 0;
for (coin of coins) {
    if (coin <= K){
        ans += Math.floor(K/coin);
        K %= coin;
        if (K === 0) {
            break;
        }
    } 
}
console.log(ans);
 