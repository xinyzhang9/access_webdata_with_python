var isMatch = function(s, p) {
    var match = new Array(s.length+1);
    match.fill(false);
    match[match.length-1] = true;
    for(var i = p.length-1; i >=0; i--){
        console.log('i ==',i);
        console.log(match);
        if(p[i] === '*'){
            //match from back to front
            for(var j = s.length-1; j >=0; j--){
                match[j] = match[j] || (match[j+1] && (p[i-1] === '.' || p[i-1] === s[j]));
            }
            i--;
        }else{ //match form front to back
            for(var j = 0; j < s.length; j++){
                match[j] = match[j+1] && (p[i] === '.' || p[i] === s[j]);
            }
            match[match.length-1] = false;
        }
    }
    console.log('final:');
    console.log(match);
    return match[0];
};

isMatch('aab','a*b');
