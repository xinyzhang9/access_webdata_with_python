/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var ROMAN = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    if(!s) return 0;
    var index = s.length-2;
    var sum = ROMAN[s[s.length-1]];
    while(index >= 0){
        if(ROMAN[s[index]] < ROMAN[s[index+1]]){
            sum -= ROMAN[s[index]];
        }else{
            sum += ROMAN[s[index]];
        }
        index -= 1;
    }
    console.log(sum);
    return sum;
};

var s = 'IV';
romanToInt(s);
