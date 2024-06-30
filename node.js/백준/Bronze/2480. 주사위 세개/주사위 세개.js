const fs =require('fs');
const [dice1, dice2, dice3] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);


let result;
if (dice1 === dice2 && dice2 === dice3){
    result = 10000+dice1*1000;
} else if (dice1 === dice2 && dice2 !== dice3 || dice1 === dice3 && dice1 !== dice2){
    result = 1000+dice1*100;
} else if (dice1 !== dice2 && dice2 === dice3) {
    result = 1000 + dice2 * 100;
} else if (dice1 !== dice2 && dice2 !== dice3 && dice3 !== dice1){
    result = Math.max(dice1, dice2, dice3) * 100;
}
console.log(result);