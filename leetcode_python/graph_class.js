function Graph(size){
	this.size = size;
	this.adjLst = new Map();
	//construct adjacent list
	for(var i = 1; i <= this.size; i++){
		this.adjLst.set(i,[]);
	}
}

Graph.prototype.connect = function(a,b){
	this.adjLst.get(a).push(b);
	this.adjLst.get(b).push(a);
}

Graph.prototype.print = function(){
	for(var i = 1; i <= this.size; i++){
		console.log(i,this.adjLst.get(i));
	}
}

Graph.prototype.shortestPath = function(s){
	var distances = new Array(this.size);
	var visited = new Set();
	distances.fill(-1);
	var stack = [s];
	distances[s-1] = 0;
	visited.add(s);
	while(stack.length){
		var curr = stack.pop();
		for(var child of this.adjLst.get(curr)){
			if(!visited.has(child)){
				stack.push(child);
				visited.add(child);
				distances[child-1] = distances[curr-1]+1;
			}
		}
	}
	console.log(distances);
	return distances;
}

Graph.prototype.findPath = function(s,t){
	if(s === t) return s;
	var parents = new Map();
	var visited = new Set();
	var stack = [s];
	visited.add(s);
	while(stack.length){
		var curr = stack.pop();
		if(curr === t){
			var path = [t];
			while(curr !== s){
				curr = parents.get(curr);
				path.push(curr);
			}
			path = path.reverse().map(function(x,i){
				return x+'->';
			}).join('');
			path = path.slice(0,path.length-2);
			console.log(path);
			return path;

		}
		for(var child of this.adjLst.get(curr)){
			if(!visited.has(child)){
				stack.push(child);
				visited.add(child);
				parents.set(child,curr);
			}
		}

	}
	return -1;
}


//test
var g = new Graph(4);
g.connect(1,2);
g.connect(1,3);
g.connect(3,4);
g.print();
g.findPath(2,4);