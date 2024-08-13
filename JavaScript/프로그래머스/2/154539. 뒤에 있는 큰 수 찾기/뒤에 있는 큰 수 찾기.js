function solution(numbers) {
    const ans = Array(numbers.length).fill(-1);
    const stack = [];
    
    numbers.forEach((e,i) => {
       if (stack.length > 0) {
           while (stack.length > 0) {
               const [element, idx] = stack.pop();
               if (element >= e) {
                   stack.push([element, idx]);
                   break;
               } else {
                   ans[idx] = e;                
               }
           }
       }
        stack.push([e, i]);
    });
    
    return ans;
    
}