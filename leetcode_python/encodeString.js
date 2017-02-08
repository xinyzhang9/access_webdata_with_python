/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var encode = function(strs) {
    var out = [];
    for(var str of strs){
        out.push(str.replace('#','##'));
    }
    return out.join('#');
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function(s) {
    if(!s) return [];
    var res = [];
    var arr = s.split('#');
    for(var str of arr){
        res.push(str.replace('##','#'));
    }
    return res;
};

var strs = ['#'];
console.log(encode(strs));
console.log((decode(encode(strs))));