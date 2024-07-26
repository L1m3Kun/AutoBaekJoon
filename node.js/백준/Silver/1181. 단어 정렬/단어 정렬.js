const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const setArr = new Set(input.slice(1));
const arr = [...setArr];
arr.sort((a,b) => {
  if (a.length !== b.length){
  	return a.length - b.length;
  } else {
    if (b > a) {
      return -1;
    } else if (b< a) {
      return 1;
    } else {
      return 0;
    }
  }
});
console.log(arr.join('\n'));