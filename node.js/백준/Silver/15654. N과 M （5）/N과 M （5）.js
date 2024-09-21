const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
arr.sort((a,b) => a-b);
const ans = [];
const solution = (start) => {
    const que = [start.toString()];
    let head = 0;
    
    while (head < que.length) {
        const edge = que[head];
        que[head++] = null;
        
        if (edge.length === M) {
            ans.push(edge.split('').map(e => arr[Number(e)]).join(' '));
            continue;
        }
        
        for (let node = 0; node < N ; node ++){
            if (!edge.includes(node.toString())){
                que.push(edge+node.toString());
            }
        }
    }
};

for (let i = 0; i < N ; i++){
    solution(i);
}

console.log(ans.join('\n'));