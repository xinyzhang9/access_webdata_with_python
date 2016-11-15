/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let res = 0;
    let sign = 1;
    let stack = [];
    s = s.replace(/\s+/g, '');
    for(let i = 0; i < s.length; i++){
        let c = s[i];
        switch(c){
            case '+':
                sign = 1;
                break;
            case '-':
                sign = -1;
                break;
            case '(':
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
                break;
            case ')':
                res = res * stack.pop() + stack.pop();
                break;
            default:
                let sum = parseInt(c);
                while(i+1 < s.length && (s[i+1] !=='+' && s[i+1] != '-' && s[i+1] != '(' && s[i+1] != ')')){
                    sum = sum * 10 + parseInt(s[i+1]);
                    i++;
                }
                res += sum * sign;
                break;
        }
    }
    return res;
};