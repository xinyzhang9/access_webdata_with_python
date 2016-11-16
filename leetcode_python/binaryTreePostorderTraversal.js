// Given a binary tree, return the postorder traversal of its nodes' values.

// For example:
// Given binary tree {1,#,2,3},
//    1
//     \
//      2
//     /
//    3
// return [3,2,1].

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
var postorderTraversal = function(root) {
    let res = [];
    if(!root) return res;
    let stack = [root];
    while(stack.length){
        let top = stack.pop();
        res.push(top.val);
        if(top.left){
            stack.push(top.left);
        }
        if(top.right){
            stack.push(top.right);
        }
    }
    return res.reverse();
};