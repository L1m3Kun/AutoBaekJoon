const moem = new Set(['a', 'e', 'i', 'o','u']);
const solution = (my_string) => Array.from(my_string).reduce((str, char) => moem.has(char) ? str: str+char,'');