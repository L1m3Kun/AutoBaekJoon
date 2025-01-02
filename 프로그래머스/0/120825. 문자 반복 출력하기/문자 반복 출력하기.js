function solution(my_string, n) {
    return Array.from(my_string).reduce((ans, char) => {
        return ans + char.repeat(n);
    }, '');
}