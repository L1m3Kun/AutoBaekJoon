const win_rules = {
    2: '0',
    0: '5',
    5: '2'
};
const solution = (rsp) => Array.from(rsp).reduce((wins, enermy) => wins+ win_rules[enermy], '');