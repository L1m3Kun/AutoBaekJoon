function solution(a, b) {
    return Math.max(Number(`${a}${b}`), (a*b)<<1);
}