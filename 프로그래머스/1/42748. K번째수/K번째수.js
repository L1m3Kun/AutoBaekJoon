const solution = (array, commands) => commands.reduce((prev, now) => {
    const [i, j, k] = now;
    const arr = array.slice(i-1, j);
    return [...(prev || []),arr.sort((a,b) => a-b)[k-1]];
    
}, [])