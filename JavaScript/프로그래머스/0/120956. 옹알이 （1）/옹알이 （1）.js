const pronounce = {
    'a': 'aya',
    'y': 'ye',
    'w': 'woo',
    'm': 'ma'
};

function solution(babbling) {
    return babbling.reduce((cnt, word) => {
        let charIdx = 0;
        while (charIdx < word.length) {
            if (word[charIdx] in pronounce){
                const canSpeak = pronounce[word[charIdx]];
                if (canSpeak === word.slice(charIdx, charIdx+canSpeak.length)) charIdx += canSpeak.length;
                else return cnt;
            }else return cnt;    
            
        }
        return cnt +1;
    },0);
}