function solution(num_list) {
    const nums = num_list.reduce((prev, now, idx) => {
        
        if (idx % 2){
            prev[1] += now
        } else {
            prev[0] += now
        }
        
        return prev;
    }, [0,0]);
    console.log(nums)
    return Math.max(...nums);
}