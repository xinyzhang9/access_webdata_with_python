/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    let res = [];
    let stack = [];
    while(stack.length || root){
        if(root){
            res.push(root.val);
            stack.push(root);
            root = root.left;
        }else{
            root = stack.pop();
            root = root.right;
        }
    }
    return res;
};

var preorderTraversal2 = function(root) {
    let res = [];
    if(!root) return [];
    let stack = [root];
    while(stack.length > 0 ){
        var p = stack.pop();
        res.push(p.val);
        if(p.right){
            stack.push(p.right);
        }
        if(p.left){
            stack.push(p.left);
        }
    }
    return res;
};