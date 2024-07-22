const fs = require('fs');
const [a, b] = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const [reverseA, reverseB] = [a.split('').reverse().join(''), b.split('').reverse().join('')];
let ans = reverseA

for (let i=0;i<3;i++){
    if (reverseA[i] > reverseB[i]){
        ans = reverseA;
        break;
    } else if (reverseA[i] < reverseB[i]){
        ans = reverseB;
        break;
    }
}
console.log(ans);