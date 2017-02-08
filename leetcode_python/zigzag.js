/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    var matrix = new Array(numRows).fill("");
    var inc = 1;
    var i = 0;
    Array.from(s).forEach((c)=>{
        matrix[i] += c;
        if(i+inc >= numRows && i-inc < 0) inc = 0;
        if(i+inc >= numRows || i+inc < 0){
            inc = -inc;
        }
        console.log(inc);
        i += inc;
    })
    
    var res = '';
    console.log(matrix);
    for(var m of matrix){
        res += m;
    }
    console.log(res);
    return res;
};

var s = 'AB';
var numRows = 1;
convert(s,numRows);