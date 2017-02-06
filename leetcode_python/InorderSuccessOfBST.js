/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */
var inorderSuccessor = function(root, p) {
    var succ = null;
    while(root){
        if(root.val > p.val){
            succ = root;
            root = root.left;
        }else{
            root = root.right;
        }
    }
    return succ;
};