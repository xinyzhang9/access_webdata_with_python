/**
 * @param {string} str
 * @returns {string}
 */
var reverseWords = function(str) {
    var arr = str.split(' ');
    var res = [];
    for(var i = arr.length-1; i >=0; i--){
        if(arr[i] !== '') res.push(arr[i]);
    }

    console.log(res.join(' '));
    return res.join(' ');
};

var str = "   a   b ";
reverseWords(str);