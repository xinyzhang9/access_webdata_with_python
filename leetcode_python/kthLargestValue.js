// Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

// For example,
// Given [3,2,1,5,6,4] and k = 2, return 5.

// Note: 
// You may assume k is always valid, 1 ≤ k ≤ array's length.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    let r = Math.floor(Math.random()*nums.length);
    let pivot = nums[r];
    let num1 = [], num2 = [];
    for(let n of nums){
        if (n > pivot){
            num1.push(n);
        }else if(n < pivot){
            num2.push(n)
        }
    }
    if (k <= num1.length){
        return findKthLargest(num1,k)
    }
    if (k > nums.length - num2.length){
        return findKthLargest(num2,k-(nums.length-num2.length))
    }
    return pivot;
};