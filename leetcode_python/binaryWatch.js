/**
 * @param {number} num
 * @return {string[]}
 */
var readBinaryWatch = function(num) {
    const hr = [8,4,2,1];
    const mi = [32,16,8,4,2,1];
    let res = [];
    for(let i = 0; i <= num; i++){
        let list1 = generateDigit(hr,i);
        let list2 = generateDigit(mi,num-i);
        for(let x of list1){
            if (x >= 12) continue;
            for(let y of list2){
                if(y >= 60) continue;
                res.push(x+':'+(y < 10?'0'+y:y));
            }
        }
    }
    return res;
    
};

function generateDigit(nums, count){
    let res = [];
    helper(nums,count,0,0,res);
    return res;
}

function helper(nums, count, pos, sum, res){
    if(count === 0){
        res.push(sum);
        return;
    }
    for(let i = pos; i < nums.length; i++){
        helper(nums,count-1,i+1,sum+nums[i],res);
    }
}