// 28278 스택 2
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");
// const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const main = (N, ...orderText) => {
  const stack = Array(N).fill(0);
  let rear = 0;
  let answer = "";
  orderText.forEach((order) => {
    const [request, num] = order.split(" ").map(Number);
    let result = undefined;
    switch (request) {
      case 1:
        stack[rear++] = num;
        break;
      case 2:
        result = rear > 0 ? stack[--rear] : -1;
        break;
      case 3:
        result = rear;
        break;
      case 4:
        result = rear > 0 ? 0 : 1;
        break;

      default:
        result = rear > 0 ? stack[rear - 1] : -1;
        break;
    }
    if (result !== undefined) {
      answer += result + "\n";
    }
  });
  console.log(answer);
};

main(...input);
