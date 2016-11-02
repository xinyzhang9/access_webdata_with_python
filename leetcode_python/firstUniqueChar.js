// Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode",
// return 2.

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let map = new Map();
    for(let i = 0; i < s.length; i++){
        if(!map.has(s[i])) map.set(s[i],1);
        else{
            map.set(s[i],map.get(s[i])+1);
        }
    }
    for(var [key,value] of map.entries()){
        if(value === 1) return s.indexOf(key);
    }
    return -1;
};