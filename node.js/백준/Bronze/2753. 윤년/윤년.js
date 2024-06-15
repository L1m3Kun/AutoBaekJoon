const year = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

if (!(year % 4) && ((year % 100) || !(year % 400))) {
    console.log(1);
} else {
    console.log(0);
}