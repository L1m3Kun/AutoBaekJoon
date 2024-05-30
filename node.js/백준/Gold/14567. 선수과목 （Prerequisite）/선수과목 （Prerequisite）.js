const fs = require("fs");

const setting = () => {
    // const input = fs.readFileSync("input.txt").toString().split("\n");
    const input = fs.readFileSync('/dev/stdin', "utf8").trim().split("\n");
    const [N, M] = input[0].split(" ").map(Number);
    const nearList = [];
    for (let i =0;i<N;i++) nearList.push([]);
    const visited = Array(N).fill(0);
    if (M === 0) return [N , M ,nearList, visited];

    let [a,b] = [0,0];

    input.slice(1, ).forEach((element) => {
        [a, b] = element.split(" ").map(Number);
        nearList[a-1].push(b-1);
        visited[b-1] ++;
    })
    return [N, M, nearList, visited];
}


const main = (N, M, nearList, visited) => {
    const queue = {};
    let front = 0;
    let rear = 0;
    const ans = Array(N).fill(1);

    for (let i=0;i<N;i++){
        if(visited[i] === 0){
            queue[rear++] = [i, 1];
        }
    }

    
    let spot = 0;
    let deg = 1;
    while (queue[front]){
        [spot, deg] = queue[front++];
        delete queue[front-1];
        if (!nearList[spot]) continue;

        for (node of nearList[spot]) {
            visited[node] --;
    
            if (visited[node] === 0) {
                queue[rear++] = [node, deg+1];
                ans[node] = deg+1;
            }
        }
    }   

    console.log(...ans);
}


const [ N, M, nearList, visited ] = setting();
main(N,M,nearList,visited);
