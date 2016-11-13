var wordBreak = function(s, wordDict) {
    let dp = new Array(s.length+1);
    dp.fill(false);
    dp[s.length] = true;
    for(let i = s.length-1; i >= 0; i--){
        for(let j = i; j < s.length; j++){
            let str = s.slice(i,j+1);
            if(wordDict.has(str) && dp[j+1]){
                dp[i] = true;
                break;
            }
        }
    }
    console.log(dp);
    return dp[0];
};

let set = new Set();
set.add('leet');
set.add('code');
wordBreak('leetcode',set)