function solution(name, yearning, photo) {
    return photo.reduce((ans, nameArray) => {
        ans.push(nameArray.reduce((score, n)=>{
            for (let i = 0; i< name.length ; i++) {
                if (n === name[i]){
                    score += yearning[i];
                    break;
                }
            }
            return score;
        },0));
        return ans;
    }, []);
}