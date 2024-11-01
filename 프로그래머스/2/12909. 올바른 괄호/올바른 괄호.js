function solution(s){
    let cnt = 0;
    breakpoint: for (let b of s){
        switch(b){
            case ')':
                cnt --;
                if (cnt <0) return false;
                break;
            default:
                cnt ++;
                break;
        }
    }
    return cnt ? false : true;
}