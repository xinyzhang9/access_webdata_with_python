/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumOfLeftLeaves = function(root) {
    if(!root) return 0;
    let res = 0;
    let stack = [root];
    while(stack.length){
        let node = stack.pop();
        if(node.left){
            stack.push(node.left);
            if(!node.left.left && !node.left.right){
                res+=node.left.val;
            }
        }
        if(node.right){
            stack.push(node.right);
        }
    }
    return res;
};