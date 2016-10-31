var threeSum = function(nums) {
    var res = [];
    if(!nums || nums.length < 3) return res;
    nums = nums.sort(function(x,y){return x-y});
    console.log(nums);
    for(var i = 0; i < nums.length-2; i++){
        if(i !== 0 && nums[i] === nums[i-1]){
            continue;
        }
        var l = i+1;
        var r = nums.length-1;
        while(l < r){
            if(nums[l]+nums[r]+nums[i] === 0){
                var tmp = [];
                tmp.push(nums[i]);
                tmp.push(nums[l]);
                tmp.push(nums[r]);
                res.push(tmp);
                l++;
                r--;
                while(l < r && nums[l] === nums[l-1]){
                    l++;
                }
                while(l < r && nums[r] === nums[r+1]){
                    r--;
                }
            }else if(nums[l]+nums[r]+nums[i] < 0){
                l++;
            }else{
                r--;
            }
        }
    }
    return res;
    
};

var res = threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]);
console.log(res);