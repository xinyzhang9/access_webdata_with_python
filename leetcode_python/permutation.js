/**
 *  swap
 */
var permute = function(nums) {
    let res = [];
    helper(0,nums);
    return res;
    
    function helper(i,nums){
        if(i === nums.length){
            res.push(nums.slice());
        }
        for(let j = i; j < nums.length; j++){
            swap(nums,i,j);
            helper(i+1,nums);
            swap(nums,i,j);
        }
    }
    
    function swap(nums,i,j){
        let tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};

/**
 *  backtrace
 */
var permute = function(nums) {
    let res = [];
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
            }
        }
        
    }
};