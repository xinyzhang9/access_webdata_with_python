/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number}
 */
var closestValue = function(root, target) {
    var root_val  = root.val;
    var kid = (target < root_val)?root.left:root.right;
    if(!kid) return root_val;
    var kid_val = closestValue(kid,target);
    return (Math.abs(root_val-target) < Math.abs(kid_val-target))?root_val:kid_val;
};

var closestValue2 = function(root, target) {
    var res = root.val;
    while(root){
        res = (Math.abs(root.val-target) < Math.abs(res-target))?root.val : res;
        root = target < root.val?root.left : root.right;
    }
    return res;
};