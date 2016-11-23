var Heap = require('Heap');

function getMedians(arr){
	var lowers = new Heap(function(a,b){return b-a;}); //maxHeap
	var highers = new Heap(); //minHeap
	var medians = [];
	for(var i = 0; i < arr.length; i++){
		var number = arr[i];
		addNumbers(number,lowers,highers);
		rebalance(lowers,highers);
		medians.push(getMedian(lowers,highers));
	}
	return medians;
}

function addNumbers(number, lowers, highers){
	if(lowers.size() === 0 || number < lowers.peek()){
		lowers.push(number);
	}else{
		highers.push(number);
	}
}

function rebalance(lowers,highers){
	var smaller = lowers.size() < highers.size()?lowers:highers;
	var bigger = lowers.size() < highers.size()?highers:lowers;

	if(bigger.size()-smaller.size() >= 2){
		smaller.push(bigger.pop());
	}
}

function getMedian(lowers,highers){
	var smaller = lowers.size() < highers.size()?lowers:highers;
	var bigger = lowers.size() < highers.size()?highers:lowers;

	if(smaller.size() === bigger.size()){
		return ((smaller.peek()+bigger.peek())/2).toFixed(1);
	}else{
		return bigger.peek();
	}
}

//test

var arr = [];
for(var i = 1; i <= 10; i++){
	arr.push(i);
}
var res = getMedians(arr);
for(var i = 0; i < res.length; i++){
	console.log(res[i]);
}