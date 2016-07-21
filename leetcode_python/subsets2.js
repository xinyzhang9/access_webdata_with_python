/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort();
    var res = [[]];
    var startIndex = 0;
    var size = 0;
    for(var i = 0; i < nums.length; i++){
        startIndex = (i > 0 && nums[i] == nums[i-1])?size:0;
        size = res.length;
        for(var j = startIndex; j < size; j++){
            var tmp = res[j].slice();
            tmp.push(nums[i]);
            res.push(tmp);
        }
    }
    return res;
};

nums = [1,2,2];
console.log(subsetsWithDup(nums))