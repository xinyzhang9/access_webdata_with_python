/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if(n > 0) return positivePow(x,n);
    else return 1/positivePow(x,-n);
    
    function positivePow(x,n){
        if(n === 0) return 1;
        let res = positivePow(x,Math.floor(n/2));
        res *= res;
        if(n % 2) res *= x;
        return res;
    }
};