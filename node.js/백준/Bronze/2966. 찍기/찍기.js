const fs = require('fs');
const [T, questions] = fs.readFileSync('/dev/stdin').toString().split('\n');
const answers = ['ABC','BABC','CCAABB'];
const names = ['Adrian','Bruno','Goran'];
const answer = Array.from(questions).reduce((ans, q, idx) => {
    answers.forEach((a, i) => {
        if (a[idx % a.length] === q){
            ans[i] ++
        }
    })
    return ans;
}, [0, 0, 0])

const maxAnswer = Math.max(...answer);
const candidate = answer.reduce((acc, a, idx) => {
    if (maxAnswer === a) {
        acc.push(names[idx]);
    }
    return acc;
}, [])
console.log(maxAnswer);
console.log(candidate.join('\n'));