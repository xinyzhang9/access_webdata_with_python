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
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var m = parseInt(n_temp[1]);
    coins = readLine().split(' ');
    coins = coins.map(Number);
    
    console.log(solve(coins,n));

}

function solve(coins,N){
    let numCoins = new Array(N+1);
    numCoins.fill(0);
    numCoins[0] = 1;
    for(let i = 0; i < coins.length; i++){
        for(let j = coins[i]; j <= N; j++){
            numCoins[j] += numCoins[j - coins[i]];
        }
    }
    return numCoins[N];
}
