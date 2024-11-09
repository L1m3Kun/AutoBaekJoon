function solution(n) {
    const sqrt = Math.sqrt(n);
    return sqrt === parseInt(sqrt) ? (sqrt+1) ** 2 : -1;
}