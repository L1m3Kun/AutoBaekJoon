const [[N, K], A] = require("fs").readFileSync("/dev/stdin")
                                 .toString()
                                 .trim()
                                 .split("\n")
                                 .map((line)=>line.split(" ").map(Number));
let k = 0;
const merge = (l, r) => {
  const mergedA = [];
  let [i, j] = [0, 0];
  while (i < l.length && j < r.length) {
    if (l[i] < r[j]) {
      mergedA.push(l[i++]);
      if (++k === K) return l[i-1];    
    }
    else {
      mergedA.push(r[j++]);
      if (++k === K) return r[j-1];
    }

  }
  while(i < l.length){
    mergedA.push(l[i++]);
    if (++k === K) return l[i-1];          
  }
  while(j < r.length) {
    mergedA.push(r[j++]);
    if(++k === K) return r[j-1];
  }
  return mergedA;
};

const mergeSort = (s, e) => {
  if (s>=e) return [A[e]];
  const mid = (s+e) >> 1;
  const left = mergeSort(s, mid);
  if (typeof left === 'number') return left;
  const right = mergeSort(mid+1, e);
  if (typeof right === 'number') return right;
  const cand = merge(left, right);
  return cand;
};
const ans = mergeSort(0, N-1);
console.log(typeof ans === "object" ? -1 : ans);