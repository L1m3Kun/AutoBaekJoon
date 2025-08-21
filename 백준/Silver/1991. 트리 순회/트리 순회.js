const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const N = Number(input[0]);
const tree = Array.from(Array(N), () => []);
input.slice(1).forEach((e) => {
    const [edge, node1, node2] = e.split(' ');
    tree[edge.charCodeAt()-65].push(node1);        
    tree[edge.charCodeAt()-65].push(node2);        
    
});

let inorder = '';
let preorder = '';
let postorder = '';

const dfs = (edge) => {
    const [left, right] = tree[edge.charCodeAt()-65];
    preorder += edge;
    if (left !== '.') dfs(left);
    inorder += edge;
    if (right !== '.') dfs(right)
    postorder += edge;    
};

dfs('A');

console.log([preorder, inorder, postorder].join('\n'));

