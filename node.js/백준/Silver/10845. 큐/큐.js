const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

class Queue {
    constructor(maxLength){
        this.queue = Array(maxLength).fill(-1);
        this.head = 0;
        this.rear = 0;
    }
    
    push(item) {
        this.queue[this.rear++] = item;
    }
    
    pop(){
        if (this.empty()) return -1;
        const poped = this.queue[this.head];
        this.queue[this.head++] = null;
        return poped;
    }
    
    size(){
        return this.rear - this.head;
    }
    
    empty(){
        return +(this.rear === this.head);
    }
        
    front(){
        if (this.empty()) return -1;
        return this.queue[this.head];
    }
        
    back(){
        if (this.empty()) return -1;
        return this.queue[this.rear - 1];
    }
}

const queue = new Queue(Number(inputs[0]));
const ans = inputs.slice(1).reduce((ans, input) => {
    const [order, item] = input.split(" ");
    switch(order) {
        case "pop":
            ans.push(queue.pop());
            break;
        case "size":
            ans.push(queue.size());
            break;
        case "empty":
            ans.push(queue.empty());
            break;
        case "front":
            ans.push(queue.front());
            break;
        case "back":
            ans.push(queue.back());
            break;
        default:
            queue.push(item);
    }
    return ans;
}, []);
console.log(ans.join("\n"));