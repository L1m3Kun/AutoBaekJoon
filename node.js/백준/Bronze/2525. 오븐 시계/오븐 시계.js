const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
let [hour, minute] = input[0].split(' ').map(Number);
const cookTime = Number(input[1]);

minute += cookTime;
if (minute >= 60) {
    hour += parseInt(minute/60);
    minute %= 60;
    hour %= 24;
}
console.log(hour, minute);