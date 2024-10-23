const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());
const ans = [];
for (let i = 0; i<n; i++){
    let star = '';
    for (let j =n-i-1; j >0; j--){
        star += ' ';
    }
    
    for (let j =0; j < i; j++){
        star += '*';
    }
    for (let j =0; j <= i; j++){
        star += '*';
    }
    ans.push(star);
}
for (let i = n-2; i>=0; i--){
    let star = '';
    for (let j =n-i-1; j >0; j--){
        star += ' ';
    }
    
    for (let j =0; j < i; j++){
        star += '*';
    }
    for (let j =0; j <= i; j++){
        star += '*';
    }
    ans.push(star);
}
console.log(ans.join('\n'));