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
var countNodes = function(root) {
    var lh = getLeftHeight(root);
    var rh = getRightHeight(root);
    if(lh === rh){
        return (1 << lh)-1;
    }else{
        return 1+countNodes(root.left)+countNodes(root.right);
    }
};

function getLeftHeight(root){
    var res = 0;
    while(root){
        root = root.left;
        res += 1;
    }
    return res;
}

function getRightHeight(root){
    var res = 0;
    while(root){
        root = root.right;
        res += 1;
    }
    return res;
}