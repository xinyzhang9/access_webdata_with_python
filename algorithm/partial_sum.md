## segment tree
```
import java.util.Scanner;  
import java.io.File;
import java.io.FileNotFoundException;

class Segment{
  class Node{
    int sum;
    int left;
    int right;
    Node leftNode;
    Node rightNode;
    Node(){
      sum = 0;
      leftNode = null;
      rightNode = null;
    }
  }
  Node root;
  
  Segment(int[] nums, int left, int right){
    root = build(nums, left, right);
  }
  
  Node build(int[] nums, int left, int right){
    if(left > right) return null;
    
    Node node = new Node();
    node.left = left;
    node.right = right;
    
    if(left == right){
      node.sum = nums[left];
    }else{
      int mid = left + (right - left)/2;
      node.leftNode = build(nums, left, mid);
      node.sum += node.leftNode.sum;
      node.rightNode = build(nums, mid+1, right);
      node.sum += node.rightNode.sum;
    }
    
    return node;
  }
  
  int getSum(int left, int right){
    return sum(root,left,right);
  }
  int sum(Node node, int left, int right){
    if(node == null || right < node.left || left > node.right) return 0;
    if(left < node.left) left = node.left;
    if(right > node.right) right = node.right;
    if(left == node.left && right == node.right) return node.sum;
    else return sum(node.leftNode, left, right) + sum(node.rightNode, left, right);
  }
  
  void update(int pos, int diff){
    updateSum(root, pos, diff);
  }
  
  void updateSum(Node node, int pos, int diff){
    if(node == null || pos < node.left || pos > node.right) return;
    node.sum += diff;
    updateSum(node.leftNode, pos, diff);
    updateSum(node.rightNode, pos, diff);
  }
}

public class SolutionSegment{
  public static void main(String[] args) throws FileNotFoundException{
    Scanner in = new Scanner(new File('input.txt'));
    
    int n = in.nextInt();
    while(n!=-1){
      int[] nums = new int[n];
      for(int i = 0; i < n; i++) nums[i] = in.nextInt();
      Segment tree = new Segment(nums, 0, n-1);
      
      in.nextLine();
      String op in.nextLine();
      while(op.equals("END") == false){
        if(op.equals('SUM)){
          int left = in.nextInt();
          int right = in.nextInt();
          System.out.println(tree.getSum(left,right));
        }else{
          int pos = in.nextInt();
          int value = in.nextInt();
          tree.update(pos, value - nums[pos]);
        }
        in.nextLine();
        op = in.nextLine();
      }
      n = in.nextInt();
    }
    in.close();
  }
}
```
## Binary index tree
```
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

class BIT{
  int[] bit;
  int left;
  int right;
  
  void build(int[] nums, int left, int right){
    bit = new int[right+1];
    this.left = left;
    this.right = right;
    
    for(int i = left; i <= right; i++){
      bit[i] = 0;
    }
    
    for(int i = left; i <= right; i++){
      for(int j = i; j <= right; j+j&(-j)){
        bit[j] += nums[j];
      }
    }
  }
  
  int getSum(int left, int right){
    return sum(right)-sum(left-1);
  }
  
  int sum(int pos){
    int result = 0;
    for(int j = pos; j > 0; j-=j&(-j)) result += bit[j];
    return result;
  }
  
  void update(int pos, int diff){
    for(int j = pos; j <= right; j+=j&(-j)) bit[j] += diff;
  }
}

public class SolutionBIT{
  public static void main(String[] args) throws FileNotFoundException{
    Scanner in = new Scanner(new File('input.txt'));
    
    int n = in.nextInt();
    while(n!=-1){
      int[] nums = new int[n+1];
      for(int i = 0; i < n; i++) nums[i] = in.nextInt();
      BIT bit = new BIT();
      bit.build(nums,1,n);
      
      in.nextLine();
      String op in.nextLine();
      while(op.equals("END") == false){
        if(op.equals('SUM)){
          int left = in.nextInt()+1;
          int right = in.nextInt()+1;
          System.out.println(bit.getSum(left,right));
        }else{
          int pos = in.nextInt()+1;
          int value = in.nextInt();
          bit.update(pos, value - nums[pos]);
        }
        in.nextLine();
        op = in.nextLine();
      }
      n = in.nextInt();
    }
    in.close();
  }
}
```
