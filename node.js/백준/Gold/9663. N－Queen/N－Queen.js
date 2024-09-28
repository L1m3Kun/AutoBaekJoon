const n = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

var cnt = 0;
const col = Array(n).fill(0);
const di = Array(n<<1 -1).fill(0);
const dj = Array(n<<1 -1).fill(0);
const bt = (start, end) => {
    if (start === end) {
        cnt ++;
        return;
    }
    for (let j = 0; j < end ; j++){
        if (!col[j] && !di[start+j] && !dj[end-j+start-1]){
            col[j] = 1;
            di[start+j] = 1;
            dj[end-1+start-j] = 1;
            bt(start+1, end);
            col[j] = 0;
            di[start+j] = 0;
            dj[end-1+start-j] = 0;
        }
    }
}
bt(0, n);
console.log(cnt);
