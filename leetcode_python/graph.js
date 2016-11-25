//for hackerrank problem
function Graph(n){ // n is number of nodes
    this.NodeMap = new Map();
    this.nodes = []; //nodes
    for(var i = 1; i <= n; i++){
    	var node = new Node(i);
    	this.nodes.push(node);
    	this.NodeMap.set(i,node);
    }

}
Graph.prototype.connect = function(s,d){

    var s_node = this.NodeMap.get(s);
    var d_node = this.NodeMap.get(d);
    if(s_node.childrenId.indexOf(d)<0){
    	s_node.children.push(d_node);
    	s_node.childrenId.push(d);
    }
    if(d_node.childrenId.indexOf(s)<0){
    	d_node.children.push(s_node);
    	d_node.childrenId.push(s);
    }
}

Graph.prototype.hasPath = function(s,d){
	this.restore();
	var count = 0;
	var startNode = this.NodeMap.get(s);
	var stack = [startNode];
	while(stack.length > 0){
		var cur_node = stack.pop();
		if(cur_node.visited) continue;
		cur_node.visited = true;
		if(cur_node.id === d){
			return true;
		}
		for(var i = 0; i < cur_node.children.length; i++){
			var child = cur_node.children[i];
			stack.push(child);
		}
	}

	return false;
}

Graph.prototype.shortestPath = function(s,d) {
  this.restore();
  if (s == d) { 
    return 0;               
  }
  var source = this.NodeMap.get(s);                        
  var queue = [ source ];
  var predecessor = new Map();
      source.visited = true;
      
  while (queue.length) {
    var u = queue.pop(); // Pop a vertex off the queue.
    for (var v of u.children) {
      if (v.visited) {
        continue;
      }
      v.visited = true;
      if (v.id === d) {   // Check if the path is complete.

        var path = [ v.id ];   // If so, backtrack through the path.
        while (u.id !== s) {
          path.push(u.id);
          u = predecessor.get(u);
        }
        path.push(u.id);
        path.reverse();
    	console.log(path);
        return path.length-1;
      }
      predecessor.set(v,u);
      queue.push(v);
    }
  }
  return -1;
}

Graph.prototype.restore = function(){
	for(var node of this.nodes){
		node.visited = false;
	}
}
function Node(id){
    this.id = id;
    this.visited = false;
    this.children = [];
    this.childrenId = [];
}

//test
var g = new Graph(4);
g.connect(1,2);
g.connect(1,3);
// console.log(g.hasPath(1,2));
// console.log(g.hasPath(1,3));
// console.log(g.hasPath(1,4));
g.shortestPath(1,2);
