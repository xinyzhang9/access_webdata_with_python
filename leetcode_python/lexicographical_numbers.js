// Given an integer n, return 1 - n in lexicographical order.

// For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

// Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    let res = new Array(n);
    let cur = 1;
    for(let i = 0; i < n; i++){
        res[i] = cur;
        if(cur * 10 <= n) cur*=10;
        else{
            if(cur >=n) cur = Math.floor(cur/10);
            cur++;
            while(cur % 10 === 0) cur = Math.floor(cur/10); //remove tailing zeros to keep lexicalorder
        }
    }
    return res;
};