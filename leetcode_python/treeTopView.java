/*
   class Node 
       int data;
       Node left;
       Node right;
*/
void top_view(Node root)
{
    List<Integer> res = new ArrayList<Integer>();
    Node tmp = root;
    while(root.left != null){
        res.add(0,root.left.data);
        root = root.left;
    }
    root = tmp;
    res.add(root.data);
    while(root.right != null){
        res.add(root.right.data);
        root = root.right;
    }
    String listString = "";

    for (Integer s : res)
    {
        listString += s + " ";
    }
    System.out.println(listString);
}