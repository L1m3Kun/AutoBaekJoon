function solution(s){

    const [p, y] = Array.from(s).reduce((prev, char) => {
        if ('pP'.includes(char)) return [prev[0]+1, prev[1]];
        if ('yY'.includes(char)) return [prev[0], prev[1]+1];
        return prev
    }, [0,0]);
    
    return p === y;
    
}