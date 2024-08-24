const fs =require('fs');
const [A,B] = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split(' ')
                .map(Number);

const que = [[A, 0]];
let head = 0;
let ans = -1;
visited = new Set([A]);

while (head < que.length) {
    const [now, cnt] = que[head];
    que[head++] = null;
    
    if (now === B) {
        ans = cnt+1;
        break;
    }
    
    for (let post of [now<<1, now*10+1]) {
        if (post <= B && !visited.has(post)) {
            visited.add(post);
            que.push([post, cnt+1]);
        }
    }
}
console.log(ans);
