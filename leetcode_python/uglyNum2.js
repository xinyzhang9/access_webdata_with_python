// Write a program to find the n-th ugly number.

// Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

// Note that 1 is typically treated as an ugly number.

// Hint:

// The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
// An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
// The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
// Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    if(n <= 0) return 0;
    let a = 0, b = 0, c = 0;
    let res = [1];
    while(res.length < n){
        let next_val = Math.min(res[a]*2,res[b]*3,res[c]*5);
        res.push(next_val);
        if(next_val === res[a]*2) a++;
        if(next_val === res[b]*3) b++;
        if(next_val === res[c]*5) c++;
    }
    //now res.length === n
    return res[n-1];
};