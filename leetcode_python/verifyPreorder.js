var verifyPreorder = function(preorder) {
    var stack = [];
    var min = Number.MIN_SAFE_INTEGER;
    for(var num of preorder){
        console.log(num, min);
        if(num < min) return false;
        while(stack.length && num > stack[stack.length-1]){
            min = stack.pop();
        }
        stack.push(num);
    }
    return true;
};

var preorder = [2,3,1];
console.log(verifyPreorder(preorder));