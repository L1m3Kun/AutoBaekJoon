const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

class AbsHeap {
    constructor () {
        this.heap = [0];
    }
    
    heappush (item) {
        this.heap.push(item);
        let edge = this.heap.length-1;
        while (edge > 0) {
            const node = edge >> 1;
            if (node >0) { 
                if (Math.abs(this.heap[edge]) < Math.abs(this.heap[node])){
                    [this.heap[edge], this.heap[node]] = [this.heap[node], this.heap[edge]];    
                } else if (Math.abs(this.heap[edge]) === Math.abs(this.heap[node])) {
                    if (this.heap[edge] < this.heap[node]) {
                        [this.heap[edge], this.heap[node]] = [this.heap[node], this.heap[edge]];    
                    }
                }
                
            }
            edge = node;
        }
    }
    
    heappop() {
        if (this.heap.length === 1) return 0;
        if (this.heap.length === 2) return this.heap.pop();
        const popItem = this.heap[1];
        this.heap[1] = this.heap.pop();
        let edge = 1;
        while (edge < this.heap.length) {
            let node = edge;
            const [left, right] = [edge << 1, (edge << 1) + 1];
            if (right < this.heap.length){
                if (Math.abs(this.heap[right]) < Math.abs(this.heap[node])){
                    node = right;
                } else if (Math.abs(this.heap[right]) === Math.abs(this.heap[node])) {
                    if (this.heap[right] < this.heap[node]) node = right;
                }
            }
            if (left < this.heap.length){
                if (Math.abs(this.heap[left]) < Math.abs(this.heap[node])){
                    node = left;
                } else if (Math.abs(this.heap[left]) === Math.abs(this.heap[node])) {
                    if (this.heap[left] < this.heap[node]) node = left;
                }
            }
            if (node === edge) break;
            [this.heap[edge], this.heap[node]] = [this.heap[node], this.heap[edge]];
            edge = node;
        }
        return popItem;
    }
}

const absHeap = new AbsHeap();
const ans = [];
input.slice(1).forEach(e => {
    if (e) {
        absHeap.heappush(e);
    } else {
        ans.push(absHeap.heappop());
    }
});

console.log(ans.join('\n'));