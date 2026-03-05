const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trimEnd().split("\n");
const n = +inputs[0]-1;
const rooms = Array.from({length: n+1}, () => []);
const reverseRooms = Array.from({length: n+1}, () => []);
const ans = ["PARDON", "LIMITED"];

let roomId = 0;
let idx = 1;
while (idx < inputs.length) {
  if (!+inputs[idx]) {
      idx += 2;
      roomId++;
      continue;
  }
  const items = inputs[idx+1].split(" ").map(Number).map((num)=> num-1);
  rooms[roomId].push(...items);
  items.forEach((item) => {
    reverseRooms[item].push(roomId);
  })
  roomId ++;
  idx += 2;
}

const bfs = (start, array)=>{
  const queue = [start];
  let head = 0;
  const visited = Array(n+1).fill(0);
  visited[start] = 1;
  while(queue.length > head) {
    const room = queue[head];
    queue[head++] = null;
    for (const nextRoom of array[room]){
      if (visited[nextRoom]) continue;
        visited[nextRoom] = 1;
        queue.push(nextRoom);
      }
  }
  return visited;
}


const reach = bfs(0, rooms);
const canReach = bfs(n, reverseRooms)
  
for (let i = 0; i <= n; i++) {
  if (reach[i] && !canReach[i]) {
    ans[0] = "PRISON"; 
    break;
  }
}


// 위상정렬

const inDegree = Array(n+1).fill(0);
const active = Array(n+1).fill(0); // 실제로 연결된 노드만 탐색
let activeCount = 0;
for (let i = 0; i <n+1; i++) {
  if (!reach[i]) continue;
  if (i === n) continue;
  if (rooms[i].length ===0) continue;
    
  activeCount ++;
  active[i] = 1;
}
for (let i = 0; i < n+1; i++){
  if (!active[i]) continue;
  const room = rooms[i];
  for (const nextRoom of room){
    if (active[nextRoom]) inDegree[nextRoom] ++;
  }
}

const queue = [];
let head = 0;
for (let i = 0; i<n+1; i++){
    if (inDegree[i]) continue;
    if (!active[i]) continue;
    queue.push(i);
}  
let remove = 0;
while(queue.length > head) {
    const room = queue[head];
    queue[head++] = null;
    remove++;
    for (const nextRoom of rooms[room]) {
        if (!active[nextRoom]) continue;
        if (--inDegree[nextRoom] > 0) continue; 
        queue.push(nextRoom);
    }
} 
if (remove !== activeCount) ans[1] = "UNLIMITED"
console.log(ans.join(" "));