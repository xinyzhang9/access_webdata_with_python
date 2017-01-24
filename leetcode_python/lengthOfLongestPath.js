var lengthLongestPath = function(input) {
    var paths = input.split("\n");
    var stack = new Array(paths.length+1).fill(0);
    var maxLen = 0;
    for(var p of paths){
        
        var lev = p.lastIndexOf('\t')+1;
        console.log(lev);
        var curLen = stack[lev+1] = stack[lev]+p.length-lev+1;
        if(p.indexOf('.') !== -1) maxLen = Math.max(maxLen, curLen - 1);
        // -1 means remove the trailing '\';
        // stack = [0,4,12,21,0] => ['','dir\','dir\subdir1\','dir\subdir1\file.ext\','']
        
    }
    
    console.log(stack);
    console.log(maxLen);
    return maxLen;
};

lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext");
