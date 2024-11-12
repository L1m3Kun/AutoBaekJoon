const solution = (arr) => arr.reduce((prev, now) => {
    if (prev[prev.length-1] !== now) prev.push(now);
    return prev
},[arr[0]])
