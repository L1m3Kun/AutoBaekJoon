function solution(arr) {
    if (arr.length === 1) return [-1]
    const minV = Math.min(...arr);
    return arr.filter((e) => e !== minV);
}