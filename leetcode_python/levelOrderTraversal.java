   /* 
    
    class Node 
       int data;
       Node left;
       Node right;
   */
   void LevelOrder(Node root)
    {
       Queue<Node> queue = new LinkedList<Node>();
       List<Integer> res = new ArrayList<Integer>();
       queue.add(root);
       while(!queue.isEmpty()){
           Node curr = queue.poll();
           res.add(curr.data);
           if(curr.left != null){
               queue.add(curr.left);
           }
           if(curr.right != null){
               queue.add(curr.right);
           }
       }
       String listString = "";

        for (Integer s : res)
        {
            listString += s + " ";
        }
        System.out.println(listString);
      
    }
