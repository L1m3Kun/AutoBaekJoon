const N = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

const arr = Array.from({length: N}, (_,i) => i+1);
let head = 0;
while (head < arr.length-1) {
    arr[head++] = null
    arr.push(arr[head]);
    arr[head++] = null
}
console.log(arr[head]);
