const [[N, K], A] = require("fs").readFileSync("/dev/stdin")
                                 .toString()
                                 .trim()
                                 .split("\n")
                                 .map((line)=>line.split(" ").map(Number));

let k = 0;
let changed = [0,0];
const quickSort = (s, e) => {
  //console.log("start: ", s, e)
  if (s >= e) return 0;
  const mid = partition(s, e);
  if (mid === -1) return -1;
  //console.log(mid);
  const left = quickSort(s, mid-1);
  //console.log("left end: ", A)
  if (left < 0) return -1;
  const right = quickSort(mid+1, e);
  //console.log("right end: ", A)
  if (right < 0) return -1;
};

const partition = (s, e) => {
  //console.log("partition: ", s, e)
  let [x, i] = [A[e], s-1];
  //console.log("    x, i:", x, i);
  for (let j = s; j < e; j++){
    if (A[j] < x) {
        i++;
        [A[i], A[j]] = [A[j], A[i]];
        //console.log("    changed: ", i, j, A)
        if (++k === K) {
          changed[0] = A[i];
          changed[1] = A[j];
          return -1;
        }
    }
    //console.log("    ", i, j, A)
  }
  if (i+1 !== e) {
      [A[i+1], A[e]] = [A[e], A[i+1]];
      //console.log("    changed: ", i+1, e, A)
      if (++k === K) {
        changed[0] = A[i+1];
        changed[1] = A[e];
        return -1;
      }
  }
  return i+1;
};

quickSort(0, N-1);
// console.log(changed)
console.log(k === K? changed.join(" ") : -1);