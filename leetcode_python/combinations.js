// Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

// For example,
// If n = 4 and k = 2, a solution is:

// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]

/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    let res = [];
    helper(res,[],1,n);
    return res;
    
    function helper(res,tmp,start,n){
        if(tmp.length === k){
            res.push(tmp.slice());
            return;
        }
        for(let i = start; i <= n; i++){
            if(tmp.length >= 1 && tmp[tmp.length-1] >= i) continue;
            tmp.push(i);
            helper(res,tmp,start+1,n);
            tmp.pop();
        }
    }
};