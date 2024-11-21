const solution = (n, control) => Array.from(control).reduce((ans, char) => {
    switch(char) {
        case 'w':
            return ans + 1;
        case 's':
            return ans - 1;
        case 'd':
            return ans + 10;
        case 'a':
            return ans - 10;
        default:
            return ans;
    }
}, n);