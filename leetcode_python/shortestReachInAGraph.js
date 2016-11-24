//pass 3/6 test cases
function processData(input) {
    //Enter your code here
    let _input = input.split('\n').map(function(x){return x.trim()});
    let cursor = 0;
    let num_query = parseInt(_input[cursor++]);
   
    while(num_query--){
        let num_nodes, num_edges;
        
        [num_nodes, num_edges] = _input[cursor++].split(' ').map(function(x){return parseInt(x)});
        let g = new Graph(num_nodes);
        while(num_edges--){
            g.connect(..._input[cursor++].split(' ').map(function(x){return parseInt(x)}));
        }
        let startNode = parseInt(_input[cursor++]);
        let res = [];
        for(let j = 1; j <= num_nodes; j++){
            if(j === startNode) continue;
            let path_length = g.shortestPath(startNode,j);
            if(path_length === -1){
                res.push(-1);
            }else{
                 res.push((path_length-1)*6);
            }
            
        }
        let str = res.join(' ');
        console.log(str);
        
    }
    
}

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

	return -1;
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
    	return path.length;
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

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
