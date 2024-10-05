const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const N = input[0];

class HeapQ {
    constructor () {
        this.heap = [0];
    }
    
    heappush(item) {
        this.heap.push(item);
        let edge = this.heap.length-1;
        while ((edge>>1) > 0) {
            const node = edge >> 1;
            if (this.heap[edge] < this.heap[node]){
                [this.heap[edge], this.heap[node]] = [this.heap[node], this.heap[edge]];
            }
            edge = node;
        }
    }
    
    heappop() {
        if (this.heap.length === 1) return 0;
        
      if (this.heap.length === 2) {
        return this.heap.pop();
      }
        const popItem = this.heap[1];
        this.heap[1] = this.heap.pop();
        let edge = 1;
        while (edge < this.heap.length) {
            let node = edge;
            const [left, right] = [node << 1, (node << 1) + 1];
            
            if (right < this.heap.length && this.heap[node] > this.heap[right]){
                node = right;
            }
            if (left < this.heap.length && this.heap[node] > this.heap[left]) {
                node = left;
            }
            if (node === edge) {
                break;
            }
            [this.heap[edge], this.heap[node]] = [this.heap[node], this.heap[edge]];
            edge = node;
        }
        return popItem;
    }
}

const heap = new HeapQ();
const ans = [];
input.slice(1).forEach((e) => {
    if (e) {
        heap.heappush(e);
    } else {
        const h = heap.heappop()
        ans.push(h);
    }
});
console.log(ans.join('\n'));