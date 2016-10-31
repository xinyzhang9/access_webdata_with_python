// Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

//     For example, given array S = {-1 2 1 -4}, and target = 1.

//     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    if(!nums || nums.length < 3){
        return -1;
    }
    nums.sort(function(x,y){return x-y});
    let best = nums[0]+nums[1]+nums[2];
    for(let i = 0; i < nums.length; i++){
        let l = i+1;
        let r = nums.length-1;
        while(l < r){
            let sum = nums[l]+nums[i]+nums[r];
            if(Math.abs(sum-target) < Math.abs(best - target)) best = sum;
            if(sum < target) l++;
            else r--;
        }
    }
    return best;
};