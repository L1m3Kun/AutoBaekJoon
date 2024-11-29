const prefixSum = (num) => Array.from({length: num} , (_, i) => i+1).reduce((sum, now) => sum+now, 0);

const solution = (price, money, count) => {
    const cost = prefixSum(count) * price;
    
    return money >= cost ? 0 : cost-money;
}