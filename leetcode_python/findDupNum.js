// Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

// Note:
// You must not modify the array (assume the array is read only).
// You must use only constant, O(1) extra space.
// Your runtime complexity should be less than O(n2).
// There is only one duplicate number in the array, but it could be repeated more than once.

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let l = 0, r = nums.length-1;
    while(l <= r){
        let mid = l + Math.floor((r-l)/2);
        let cnt = 0;
        for(let i = 0; i < nums.length; i++){
            if(nums[i] <= mid) cnt++;
        }
        if(cnt > mid) r = mid-1;
        else l = mid+1;
    }
    return l;
};