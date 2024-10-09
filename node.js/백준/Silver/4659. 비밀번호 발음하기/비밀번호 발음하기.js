const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const ansForm = (str, isAccept) =>
  `<${str}> is ${isAccept ? "acceptable" : "not acceptable"}.`;

const moem = ["a", "e", "i", "o", "u"];

const hasAEIOU = (str) => {
  for (let m of moem) {
    if (str.includes(m)) return true;
  }
  return false;
};

const noContinuousThird = (str) => {
  let Mcnt = 0,
    Jcnt = 0;
  for (let i = 0; i < str.length; i++) {
    if (moem.includes(str[i])) {
      Mcnt++;
      Jcnt = 0;
      if (Mcnt >= 3) {
        return false;
      }
    } else {
      Mcnt = 0;
      Jcnt++;
      if (Jcnt >= 3) {
        return false;
      }
    }
  }
  return true;
};

const noContinuous = (str) => {
  for (let i = 1; i < str.length; i++) {
    if (str[i] === str[i - 1]) {
      if (!["e", "o"].includes(str[i])) {
        return false;
      }
    }
  }

  return true;
};

const ans = input.slice(0, input.length - 1).map((e) => {
  let isAccept = true;
  if (!hasAEIOU(e) || !noContinuousThird(e) || !noContinuous(e))
    isAccept = false;
  return ansForm(e, isAccept);
});

console.log(ans.join("\n"));
