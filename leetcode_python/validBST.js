/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    let max = Number.MAX_SAFE_INTEGER;
    let min = Number.MIN_SAFE_INTEGER;
    return helper(root,min,max);
    
    function helper(root,min,max){
        if(!root) return true;
        if(root.val <= min) return false;
        if(root.val >= max) return false;
        return helper(root.left,min,root.val) && helper(root.right,root.val,max);
    }
};