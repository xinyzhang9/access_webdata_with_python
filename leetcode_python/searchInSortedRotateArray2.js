/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    return helper(nums,0,nums.length-1) >= 0;
    
    function helper(nums,low,high){
        if(low > high) return -1;
        let mid = low + Math.floor((high-low)/2);
        if(nums[mid] == target) return mid;
        if(nums[mid] < nums[high]){
            if(target > nums[mid] && target <= nums[high]){ //in the sorted part of array
                return helper(nums,mid+1,high);
            }else{ //in the unsorted part of array
                return helper(nums,low,mid-1);
            }
        }else if(nums[mid] > nums[high]){
            if(target >= nums[low] && target < nums[mid]){ //in the sorted part of array
                return helper(nums,low,mid-1);
            }else{ //in the unsorted part of array
                return helper(nums,mid+1,high);
            }
        }else{
            return helper(nums,low,high-1);
        }
    }
};