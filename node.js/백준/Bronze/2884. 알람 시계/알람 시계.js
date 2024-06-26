const fs = require('fs');
let [hour, minute] = fs.readFileSync(0, 'utf-8').toString().trim().split(' ').map(Number);

minute -= 45;
if (minute <0){
    hour --;
    minute += 60;
    if (hour < 0){
        hour += 24;
    }
}
console.log(hour, minute);