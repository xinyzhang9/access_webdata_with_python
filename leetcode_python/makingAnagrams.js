process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var a = readLine();
    var b = readLine();
    console.log(solve(a,b));

}

function solve(a,b){
    let map1 = new Array(26);
    let map2 = new Array(26);
    let res = 0;
    map1.fill(0);
    map2.fill(0);
    for(let i = 0; i < a.length; i++){
        map1[a[i].charCodeAt(0)-'a'.charCodeAt(0)]++;
    }
    for(let i = 0; i < b.length; i++){
        map2[b[i].charCodeAt(0)-'a'.charCodeAt(0)]++;
    }
    for(let i = 0; i < 26; i++){
        res += Math.abs(map1[i]-map2[i]);
    }
    return res;
}
