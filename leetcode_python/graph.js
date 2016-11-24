function Graph(n){ // n is number of nodes
    this.NodeMap = new Map();
    this.nodes = []; //nodes
    for(var i = 1; i <= n; i++){
    	var node = new Node(i);
    	this.nodes.push(node);
    	NodeMap.set(i,node);
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
			var child = cur_node.children(i);
			stack.push(child);
		}
	}
}

function Node(id){
    this.id = id;
    this.visited = false;
    this.children = [];
    this.childrenId = [];

}