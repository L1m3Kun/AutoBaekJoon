function solution(num_list) {
    const [last, lastest] = num_list.slice(num_list.length-2);
    if (last < lastest) num_list.push(lastest - last);
    else num_list.push(lastest * 2);
    return num_list;
}