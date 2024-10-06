const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const N = Number(input[0]);

class MaxHeap {
    constructor () {
        this.heap = [0];
    }
    
    swap (left, right) {
        [this.heap[left], this.heap[right]] = [this.heap[right], this.heap[left]];
        return;
    }
    
    heappush (item) {
        this.heap.push(item);
        let edge = this.heap.length-1;
        while (edge > 0) {
            const node = edge >> 1;
            if (node > 0 && this.heap[node] < this.heap[edge]) {
                this.swap(node, edge);
            }
            edge = node;
        }
    }
    
    heappop () {
        if (this.heap.length === 1) return 0;
        if (this.heap.length === 2) return this.heap.pop();
        const popItem = this.heap[1];
        this.heap[1] = this.heap.pop();
        let edge = 1;
        while (edge < this.heap.length) {
            let node = edge;
            let [left, right] = [node << 1, (node << 1) + 1]
            if (right < this.heap.length && this.heap[right] > this.heap[node]) node = right;
            if (left < this.heap.length && this.heap[left] > this.heap[node]) node = left;
            if (node === edge) break;
            this.swap(node, edge);
            edge = node;
        }
        return popItem;
    }
}

const ans = [];
const heap = new MaxHeap();

input.slice(1).forEach(e => {
    if (e) heap.heappush(e);
    else ans.push(heap.heappop());

});
console.log(ans.join('\n'));