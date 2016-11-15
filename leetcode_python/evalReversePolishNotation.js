// Evaluate the value of an arithmetic expression in Reverse Polish Notation.

// Valid operators are +, -, *, /. Each operand may be an integer or another expression.

// Some examples:
//   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
//   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

var evalRPN = function(tokens) {
    let stack = [];
    for(let c of tokens){
        switch(c){
            case '+':
                stack.push(stack.pop()+stack.pop());
                break;
            case '-':
                stack.push(-stack.pop()+stack.pop());
                break;
            case '*':
                stack.push(stack.pop()*stack.pop());
                break;
            case '/':
                let b = stack.pop();
                let a = stack.pop();
                stack.push((a/b) >> 0); // correct way to round '/'
                break;
            default:
                stack.push(parseInt(c));
        }
    }
    return stack.pop();
        
};