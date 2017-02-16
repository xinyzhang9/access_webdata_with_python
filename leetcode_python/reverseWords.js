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

    // console.log(res.join(' '));
    return res.join(' ');
};


// var reverseWords2 = function(str) {
//     var left = 0;
//     for(var i = 0; i < str.length; i++){
//         if(i == str.length || str[i] === ' '){
//             reverse(str,left,i-1);
//             left = i+1;
//         }
//     }
//     reverse(str,0, str.length-1);
// };

// function reverse(s,left,right){
//     while(left < right){
//     	var tmp = s.charAt(left);
//     	s.replaceAt(left,s.charAt(right));
//     	s.replaceAt(right,tmp);
//     	left++;
//     	right--;
//     }
// }

// String.prototype.replaceAt=function(index, character) {
//     return this.substr(0, index) + character + this.substr(index+character.length);
// }

var str = "   a   b ";
reverseWords(str);

// var str = 'a b';
// reverseWords2(str)
// var s = 'abc';
// reverse(s,0,2);
// console.log(s);