// '?' Matches any single character.
// '*' Matches any sequence of characters (including the empty sequence).

// The matching should cover the entire input string (not partial).

// The function prototype should be:
// bool isMatch(const char *s, const char *p)

// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "*") → true
// isMatch("aa", "a*") → true
// isMatch("ab", "?*") → true
// isMatch("aab", "c*a*b") → false

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let idxs = 0, idxp = 0, idxstar = -1, idxmatch = 0;
    while(idxs < s.length){
        if(idxp < p.length && (s[idxs] === p[idxp] || p[idxp] === '?')){
            idxs++;
            idxp++;
        }else if(idxp < p.length && p[idxp] === '*'){
            idxstar = idxp;
            idxmatch = idxs;
            idxp++;
        }else if(idxstar !== -1){
            idxp = idxstar + 1;
            idxmatch++;
            idxs = idxmatch;
        }else{
            return false;
        }
    }
    while(idxp < p.length && p[idxp] === '*') idxp++;
    return idxp === p.length;
};