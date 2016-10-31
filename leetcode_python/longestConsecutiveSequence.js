// Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

// For example,
// Given [100, 4, 200, 1, 3, 2],
// The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

// Your algorithm should run in O(n) complexity.

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let res = 1;
    let hashset = new Set();
    nums.forEach(function(x){
        hashset.add(x);
    })
    
    nums.forEach(function(x){
        let cnt = 1;
        let left = x-1;
        let right = x+1;
        while(hashset.has(left)){
            hashset.delete(left);
            left--;
            cnt++;
        }
        while(hashset.has(right)){
            hashset.delete(right);
            right++;
            cnt++;
        }
        res = Math.max(cnt,res);
    })
    return res;
};