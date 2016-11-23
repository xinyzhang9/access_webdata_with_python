// Given a non-empty array of integers, return the k most frequent elements.

// For example,
// Given [1,1,1,2,2,3] and k = 2, return [1,2].

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = new Map();
    for(let n of nums){
        if(!map.has(n)){
            map.set(n,1);
        }else{
            map.set(n,map.get(n)+1)
        }
    }
    
    let sortable = [];
    for(let [k,v] of map.entries()){
        sortable.push([k,v]);
    }
    
    sortable.sort(function(a,b){return b[1]-a[1];});
    
    return sortable.map(function(x){return x[0]}).slice(0,k);

};