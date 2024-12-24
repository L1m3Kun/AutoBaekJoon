function solution(numbers) {
    let maxValue = 0;
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j ++) {
            const multipleNumber = numbers[i] * numbers[j];
            maxValue = maxValue < multipleNumber ? multipleNumber : maxValue;
        }
    }
    return maxValue;
}