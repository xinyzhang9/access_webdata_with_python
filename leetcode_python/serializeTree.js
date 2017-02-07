function TreeNode(val){
	this.val = val;
	this.left = null;
	this.right = null;
	return this;
}

function serialize(root){
	if(!root) return [];
    var stack = [root];
    var res = [];
    while(stack.length > 0){
        var p = stack.pop();
        res.push(p.val);
        if(!p.left && !p.right){
            res.push('#');
            res.push('#');
        }
        if(p.right){
            stack.push(p.right);
        }
        if(p.left){
            stack.push(p.left);
        }
    }
    return res.toString();
}

function deserialize(str){
	if(!str || str.length < 1) return null;
	var arr = str.split(',');
	var root = helper(arr);
	return root;

	function helper(arr){
		if(arr.length < 1) return null;
		var val = arr.shift();
		if(val === '#') return null;
		var p = new TreeNode(parseInt(val));
		p.left = helper(arr);
		p.right = helper(arr);
		return p;
	}
}

// test
var root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.right.left = new TreeNode(4);
root.right.right = new TreeNode(5);


var str = serialize(root);
var tree = deserialize(str);
var str2 = serialize(tree);
console.log(str);
console.log(str2);