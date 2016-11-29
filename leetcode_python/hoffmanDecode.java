/*
Sample Input

         {ϕ,5}
      0 /     \ 1
     {ϕ,2}   {A,3}
    0/   \1
{B,1}  {C,1}  

S="1001011"
Sample Output

ABACA

*/

/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String S ,Node root)
    {
        int curr = 0;
        Node old = root;
        String s = "";
        while(curr < S.length()){
            root = old;
            while(!(root.left == null && root.right == null)){
                if(S.charAt(curr) == '0'){
                    root = root.left;
                }else{
                    root = root.right;
                }
                curr++;
            }
            s += root.data;
        }
        System.out.println(s);
       
    }



