'use strict'
var lengthOfLongestSubstringKDistinct = function(s, k) {
    let map = new Map();
    let low = 0, res = 0;
    Array.from(s).forEach(function(c,i){
        map.set(c,i);
        if(map.size > k){
            low = Math.min(...Array.from(map.values()));
            map.delete(s.charAt(low));
            low+=1;
        }
        res = Math.max(i-low+1,res);
    })
    return res;
};

var s = 'eceba';
var k = 2;
console.log(lengthOfLongestSubstringKDistinct(s,k))