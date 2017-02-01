'use strict'
function ListNode(val) {
    this.val = val;
    this.next = null;
}


function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    if(!head) return null;
    return toBST(head,null);
};

var toBST = function(head,tail){
    let slow = head;
    let fast = head;
    while(fast !== tail && fast.next !== tail){
        fast = fast.next.next;
        slow = slow.next;
    }
    let root = new TreeNode(slow.val);
    root.left = toBST(head,slow);
    root.right = toBST(slow.next, tail);
    return root;
}

var head = new ListNode(0);
console.log(sortedListToBST(head));