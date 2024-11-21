const controler = {
    'w': (n) => n+1,
    's': (n) => n-1,
    'd': (n) => n+10,
    'a': (n) => n-10,
};

const solution = (n, control) => Array.from(control).reduce((ans, char) => controler[char](ans), n);