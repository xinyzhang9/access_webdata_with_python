// Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

// Example 1:
// Input: [3, 2, 1]

// Output: 1

// Explanation: The third maximum is 1.
// Example 2:
// Input: [1, 2]

// Output: 2

// Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
// Example 3:
// Input: [2, 2, 3, 1]

// Output: 1

// Explanation: Note that the third maximum here means the third maximum distinct number.
// Both numbers with value 2 are both considered as second maximum.

/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let m1 = Number.MIN_SAFE_INTEGER, m2 = Number.MIN_SAFE_INTEGER, m3 = Number.MIN_SAFE_INTEGER;
    for(let n of nums){
        if(n === m1 || n === m2 || n === m3) continue;
        if(n > m1){
            m3 = m2;
            m2 = m1;
            m1 = n;
        }else if(n > m2){
            m3 = m2;
            m2 = n;
        }else if(n > m3){
            m3 = n;
        }
    }
    return (m3 === Number.MIN_SAFE_INTEGER)?m1:m3;
};