/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} key
 * @return {TreeNode}
 */
var deleteNode = function(root, key) {
    if(!root) return null;
    if(key < root.val){
        root.left = deleteNode(root.left,key);
    }else if(key > root.val){
        root.right = deleteNode(root.right,key);
    }else{
        if(!root.left) return root.right;
        if(!root.right) return root.left;
        root.val = findMin(root.right);
        root.right = deleteNode(root.right,root.val);
    }
    return root;
};

function findMin(root){
    while(root.left){
        root = root.left;
    }
    return root.val;
}