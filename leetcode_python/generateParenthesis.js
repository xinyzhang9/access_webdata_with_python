/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let res = [];
    dfs(res,'',n,0,0);
    return res;
    
    function dfs(res,str,max,open,close){
        if(str.length === 2 * max){
            res.push(str);
            return;
        }
        if(open < max){
            dfs(res,str+'(',max,open+1,close);
        }
        if(open > close){
            dfs(res,str+')',max,open,close+1)
        }
    }
};