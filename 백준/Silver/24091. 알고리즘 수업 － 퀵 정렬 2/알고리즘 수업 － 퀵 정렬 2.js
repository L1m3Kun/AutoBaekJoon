const [[N, K], A] = require("fs").readFileSync("/dev/stdin")
                                 .toString()
                                 .trim()
                                 .split("\n")
                                 .map((line) => line.split(" ").map(Number));

let k = 0;
const partition = (s, e) => {
  let [x, i] = [A[e], s-1];
  //console.log("partition x, i: ", x, i);
  for (let j = s; j < e; j++){
    if (A[j] >= x) continue;
    i++;
    [A[i], A[j]] = [A[j], A[i]];
    //console.log("    changed: ", i, j, A);
    if (++k === K) return -1;
  }
  if (i+1 === e) return i+1;
  [A[i+1], A[e]] = [A[e], A[i+1]];
  //console.log("     changed: ", i+1, e, A);
  return ++k === K ? -1 : i+1;
}

const quickSort = (s, e) => {
  //console.log("start: ", s, e);
  if (s >= e) return 0;
  const mid = partition(s, e);
  if (mid < 0) return mid;
  const left = quickSort(s, mid-1);
  //console.log("left end: ", A);
  if (left < 0) return left;
  const right = quickSort(mid+1, e);
  //console.log("right end: ", A);
  if (right < 0) return right;
};

quickSort(0, N-1);
console.log(k === K ? A.join(" ") : -1);