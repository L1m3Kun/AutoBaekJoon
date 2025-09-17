const fs = require("fs");
const inputs = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const makeTree = (preorder) => {
  let idx = 0;
  const dfs = (min, max) => {
    if (idx >= preorder.length) return 0;
    const value = preorder[idx];
    if (value < min || value > max) return 0;
    idx++;
    return {
      value,
      left: dfs(min, value),
      right: dfs(value, max),
    };
  };

  return dfs(0, 1000000);
};

const tree = makeTree(inputs);
let ans = [];

const postorder = (node) => {
  const { left, right } = node;
  if (left) postorder(left);
  if (right) postorder(right);
  ans.push(node.value);
};

postorder(tree);
console.log(ans.join("\n"));
