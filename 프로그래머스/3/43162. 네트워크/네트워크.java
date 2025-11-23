import java.util.*;

class Solution {
    
    public void dfs(int depth, int[][] computers, int n, boolean[] visited) {
        visited[depth] = true;
        
        for (int i = 0; i < n; i++) {
            if (visited[i] == false && computers[depth][i] == 1) {
                dfs(i, computers, n, visited);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, computers, n, visited);
                answer++;
            }
        }
        
        return answer;
    }
}