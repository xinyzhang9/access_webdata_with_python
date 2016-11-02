var lengthLongestPath = function(input) {
    // console.log(input.length);
    var paths = input.split('\n');
    console.log(paths);
    var stack = new Array(paths.length+1);
    stack.fill(0);
    var maxLen = 0;
    paths.forEach(function(p){
        var lev = p.lastIndexOf('\t')+1;
        var curLen = stack[lev+1] = stack[lev]+p.length-lev+1;
        console.log(curLen);
        if(p.indexOf('.') >=0) maxLen = Math.max(maxLen,curLen-1);
        // console.log(stack);
    })

    console.log(maxLen);
    
    return maxLen;
};

lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext");
