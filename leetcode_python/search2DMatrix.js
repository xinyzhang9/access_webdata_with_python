// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.
// For example,

// Consider the following matrix:

// [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// Given target = 3, return true.

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let m = matrix.length;
    let n = matrix[0].length;
    let l = 0;
    let r = m*n-1;
    matrix = [].concat.apply([],matrix); //reduce to 1D array
    while(l <= r){
        let mid = l + Math.floor((r-l)/2);
        if(matrix[mid] === target) return true;
        else if(matrix[mid] < target){
            l = mid+1;
        }else{
            r = mid-1;
        }
    }
    return false;
};