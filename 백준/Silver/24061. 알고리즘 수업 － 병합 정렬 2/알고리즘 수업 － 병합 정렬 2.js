const [[N, K], A] = require("fs").readFileSync("/dev/stdin")
                                 .toString()
                                 .trim()
                                 .split("\n")
                                 .map((line) => line.split(" ").map(Number));


let k = 0;

const merge = (s, mid, e) => {
 // console.log("merge start: ", s, mid, e);
  let [i, j] = [s, mid+1];
  const tmp = [];
  while (i <= mid && j <= e) {
    if (A[i] <= A[j]){
      tmp.push(A[i++]);
    } else {
      tmp.push(A[j++]);
    }
  }
  for (i; i<=mid; i++) {
    tmp.push(A[i]);
  }
  for (j; j<=e; j++){
    tmp.push(A[j]);
  }
  
  for (let t = 0; t < tmp.length; t++){
    A[s+t] = tmp[t];
    if (++k === K) return 1;
    //console.log("merging A: ", A)
  }
//  console.log("merge complete: ", A);
  return 0;
};

const mergeSort = (s, e) => {
 // console.log("start: ", s, e)
  if (s >= e) return 0;
  const mid = (s+e) >> 1;
  const left = mergeSort(s, mid);
  if (left) return 1;
 // console.log("after left: ", s, mid, A)
  const right = mergeSort(mid+1, e);
  if (right) return 1;
 // console.log("after right: ", mid, e, A)
  const cand = merge(s, mid, e);
  if (cand) return 1; 
  return 0;
};
mergeSort(0, N-1);
console.log(k < K ? -1 : A.join(" "));