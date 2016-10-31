/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let u = new Union(nums.length);
    let map = new Map();
    for(let i = 0; i < nums.length; i++){
        if(map.has(nums[i])) continue;
        map.set(nums[i],i);
        if(map.has(nums[i]-1)){
            u.union(i,map.get(nums[i]-1));
        }
        if(map.has(nums[i]+1)){
            u.union(i,map.get(nums[i]+1));
        }
    }
    return u.maxUnion();
};

class Union{
    constructor(n){
        this.unions = [];
        this.size = [];
        this.count = n;
        for(let i = 0; i < n; i++){
            this.unions.push(i);
            this.size.push(1);
        }
    }
    find(p){
        if(p >= this.unions.length) return -1;
        while(p != this.unions[p]) p = this.unions[p];
        return p;
    }
    connected(p,q){
        p = this.find(p);
        q = this.find(q);
        return p === q;
    }
    union(p,q){
        p = this.find(p);
        q = this.find(q);
        if(this.size[p] > this.size[q]){
            this.size[p] += this.size[q];
            this.unions[q] = p;
        }else{
            this.size[q] += this.size[p];
            this.unions[p] = q;
        }
        this.count--;
    }
    maxUnion(){
        let max = 1;
        for(let i = 0; i < this.unions.length; i++){
            max = Math.max(max,this.size[i]);
        }
        return max;
    }
    
}