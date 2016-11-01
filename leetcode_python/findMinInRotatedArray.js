/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let l = 0;
    let r = nums.length-1;
    if(nums[l] <= nums[r]) return nums[l];
    while(l <= r){
        let mid = l + Math.floor((r-l)/2);
        if(mid >= 1 && nums[mid] < nums[mid-1]) return nums[mid];
        if(nums[mid] < nums[r]){
            r = mid-1;
        }else{
            l = mid+1;
        }
    }
};