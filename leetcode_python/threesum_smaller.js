// Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

// For example, given nums = [-2, 0, 1, 3], and target = 2.

// Return 2. Because there are two triplets which sums are less than 2:

// [-2, 0, 1]
// [-2, 0, 3]

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumSmaller = function(nums, target) {
    let cnt = 0;
    let res = [];
    if(!nums || nums.length < 3) return 0;
    nums.sort(function(x,y){return x-y;});
    for(let i = 0; i < nums.length-2; i++){
        let l = i+1;
        let r = nums.length-1;
        while(l < r){
            let sum = nums[i]+nums[l]+nums[r];
            if(sum >= target){
                r--;
            }else{
                cnt += r - l;
                l++;
            }
        }
    }
    return cnt;
};