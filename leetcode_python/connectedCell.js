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
let cellCount = 0; //better not to use global variable;
function getBiggestRegion(grid){
    
    let n = grid.length;
    let m = grid[0].length;
    let maxNum = 0;
    
    let visited = new Array(n);
    for(let i = 0; i < n; i++){
        visited[i] = new Array(m).fill(false);
    }
    const actions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]];
    for(let i = 0; i < n; i++){
        for(let j = 0; j < m; j++){
            dfs(grid,visited,i,j,n,m,actions);
            if(cellCount > maxNum) maxNum = cellCount;
            cellCount = 0;
        }
    }
    return maxNum;
    
}

function dfs(grid, visited, i, j, n, m,actions){
    if( i < 0 || i >= n || j < 0 || j >= m) return;
    if(visited[i][j] || grid[i][j] == 0) return;
    visited[i][j] = true;
    cellCount++;
    for(a of actions){
        dfs(grid,visited,i+a[0],j+a[1],n,m,actions);
    }
}

function main() {
    var n = parseInt(readLine());
    var m = parseInt(readLine());
    var grid = [];
    for(grid_i = 0; grid_i < n; grid_i++){
       grid[grid_i] = readLine().split(' ');
       grid[grid_i] = grid[grid_i].map(Number);
    }
    console.log(getBiggestRegion(grid));

}
