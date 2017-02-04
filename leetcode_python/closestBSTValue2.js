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
 * @param {number} k
 * @return {number[]}
 */
var closestKValues = function(root, target, k) {
  var res = [];
  var pred = [];
  var succ = [];
  var cur = root;
  while(cur){
      if(target > cur.val){
          pred.push(cur);
          cur = cur.right;
      }else{
          succ.push(cur);
          cur = cur.left;
      }
  }
  while(k > 0){
      if(pred.length === 0 && succ.length === 0){
          break;
      }else if(pred.length === 0){
          res.push(getSucc(succ));
      }else if(succ.length === 0){
          res.push(getPred(pred));
      }else if(Math.abs(target-pred[pred.length-1].val) < Math.abs(target-succ[succ.length-1].val)){
          res.push(getPred(pred));
      }else{
          res.push(getSucc(succ));
      }
      k--;
  }
  return res;
  
};

function getSucc(arr){
    var popped = arr.pop();
    var p = popped.right;
    while(p){
        arr.push(p);
        p = p.left;
    }
    return popped.val;
}

function getPred(arr){
    var popped = arr.pop();
    var p = popped.left;
    while(p){
        arr.push(p);
        p = p.right;
    }
    return popped.val;
}