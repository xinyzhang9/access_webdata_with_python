// Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

// Example:

// Input:
// [1,2,3]

// Output:
// 3

// Explanation:
// Only three moves are needed (remember each move increments two elements):

// [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
    return nums.reduce(function(a,b){return a+b})-nums.length * Math.min(...nums);
};