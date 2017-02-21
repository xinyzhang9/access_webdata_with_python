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
var countUnivalSubtrees = function(root) {
    var count = 0;
    helper(root);
    return count;
    
    function helper(root){
        if(!root) return true;
        var left = helper(root.left);
        var right = helper(root.right);
        if(left && right){
            if(root.left && root.left.val !== root.val) return false;
            if(root.right && root.right.val !== root.val) return false;
            count++;
            return true;
        }
        return false;
    }
};