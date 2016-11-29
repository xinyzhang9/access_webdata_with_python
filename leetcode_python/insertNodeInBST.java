 /* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

static Node Insert(Node root,int value)
    {
        if(root == null){
            root = new Node();
            root.data = value;
            return root;
        }
        Node tmp = root;
        Node last = null;
        while(tmp != null){
            last = tmp;
            if(tmp.data > value){
                tmp = tmp.left;
            }else{
                tmp = tmp.right;
            }
        }
        if(last != null){
            if(last.data > value){
                last.left = new Node();
                last.left.data = value;
            }else{
                last.right = new Node();
                last.right.data = value;
            }
        }
        return root;
       
    }


