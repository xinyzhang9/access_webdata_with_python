import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static int cellCounter = 0;
    static int[][] actionCosts = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
    
    public static int getBiggestRegion(int[][] matrix, int n, int m) {
        int[][] visited = new int[n][m];
        int maxNum = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                dfs(matrix,visited,i,j,n,m);
                if(cellCounter > maxNum) maxNum = cellCounter;
                cellCounter = 0;
            }
        }
        return maxNum;
    }
    
    private static void dfs(int[][] matrix, int[][] visited, int i, int j, int n, int m){
        if(i < 0 || i >= n || j < 0 || j >= m) return;
        if(visited[i][j] == 1 || matrix[i][j] == 0) return;
        cellCounter++;
        visited[i][j] = 1;
        for(int di = 0; di < 8; di++){
            dfs(matrix,visited,i+actionCosts[di][0],j+actionCosts[di][1],n,m);
        }
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int grid[][] = new int[n][m];
        for(int grid_i=0; grid_i < n; grid_i++){
            for(int grid_j=0; grid_j < m; grid_j++){
                grid[grid_i][grid_j] = in.nextInt();
            }
        }
        System.out.println(getBiggestRegion(grid,n,m));
    }
}
