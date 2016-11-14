## QuickSelect
```
import java.io.*;
import java.util.*;

class Quicker{
  int select(int[] nums, int k){
    return select(nums, 0, nums.length-1,k-1);
  }
  int select(int[] nums, int start, int end, int k){
    int divider = nums[end];
    int left = start;
    for(int i = start; i < end; i++){
      if(nums[i] < divider) swap(nums, i, left++);
    }
    if(left == k) return nums[end];
    if(left < k) return select(nums, left, end-1, k-(left-start)-1); //?？ if left == 0?
    else return select(nums, start, left-1, k);
  }
  
  void swap(int[] nums, int i, int j){
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
  }
}

public class Solution{
  public static void main(String[] args) throws FileNotFoundException{
    Scanner in = new Scanner(new File('input.txt'));
    
    int n = in.nextInt();
    Quick quicker = new Quicker();
    while(n!=-1){
      int[] nums = new int[n];
      for(int i = 0; i < n; i++) nums[i] = in.nextInt();
      int m = in.nextInt();
      while(m-- ！= 0){
        Syetem.out.println(quicker.select(nums, in,nextInt()));
      }
      n = in.nextInt();
    }
    in.close();
  }
}
```
