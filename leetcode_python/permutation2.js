// Given a collection of numbers that might contain duplicates, return all possible unique permutations.

// For example,
// [1,1,2] have the following unique permutations:
// [
//   [1,1,2],
//   [1,2,1],
//   [2,1,1]
// ]

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let res = [];
    nums.sort(function(a,b){return a-b;});
    let visited = new Array(nums.length);
    visited.fill(false);
    let tmp = [];
    helper(nums,tmp);
    return res;
    
    function helper(nums,tmp){
        if(tmp.length === nums.length){
            res.push(tmp.slice());
        }else{
            for(let i = 0; i < nums.length; i++){
                if(visited[i]) continue;
                visited[i] = true;
                tmp.push(nums[i]);
                helper(nums,tmp);
                tmp.pop();
                visited[i] = false;
                while(i < nums.length-1 && nums[i] === nums[i+1]) i++;
            }
        }
    }
};