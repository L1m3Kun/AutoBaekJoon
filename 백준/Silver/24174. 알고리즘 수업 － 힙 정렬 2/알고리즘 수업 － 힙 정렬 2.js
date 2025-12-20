const [[N, K], A] = require("fs").readFileSync("/dev/stdin")
                                 .toString()
                                 .trim()
                                 .split("\n")
                                 .map((line) => line.split(" ").map(Number));

let k = 0;

const heapify = (A, node, n) => {
    let [left, right] = [(node << 1) + 1, (node<<1) + 2];
    //console.log("node, left, right: ", node, left, right);
    let smaller = -1;
    if (right <= n) smaller = A[left] < A[right] ? left : right;
    else if (left <= n) smaller = left;
    else return;
    //console.log("    smaller: ", smaller);
    if (A[smaller] < A[node]) {
        [A[node], A[smaller]] = [A[smaller], A[node]];
        //console.log("    changed: ", smaller, node, A)
        //console.log("    k: ", k)
        if (++k===K) return -1;      
        const flag = heapify(A, smaller, n);
        if (flag < 0) return -1;

    }
}
  
const buildMinHeap = (A, n) => {
  //console.log("==build==")
  for (let i = (n >> 1); i >= 0; i--){
      const flag = heapify(A, i, n);
      if (flag < 0) return -1;
  }
}



const heapSort = (A) => {
  const flag = buildMinHeap(A, N-1);
  if (flag < 0) return;
  //console.log("==sort==")
  for (let i = N-1; i > 0; i--) {
      [A[0], A[i]] = [A[i], A[0]];
      //console.log("    changed: ", 0, i, A);
      //console.log("    k: ", k)
      if (++k===K) return ;
      const flag = heapify(A, 0, i-1);
      if (flag < 0) return;
  }  
};

heapSort(A);
console.log(k>=K ? A.join(" ") : -1);