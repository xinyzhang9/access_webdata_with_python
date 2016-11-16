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