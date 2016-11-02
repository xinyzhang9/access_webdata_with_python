// Sort Characters By Frequency

/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    let map = new Map();
    let res = '';
    for(let i = 0; i < s.length; i++){
        if(!map.has(s[i])) map.set(s[i],1);
        else{
            map.set(s[i],map.get(s[i])+1);
        }
    }
    let newMap = [...map].sort((a,b)=>(b[1]-a[1]));
    for(var k of newMap){
        res+=k[0].repeat(k[1]);
    }
    return res;
};