import java.util.*;

class Solution {
    static int[][] visited;
    
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public void bfs(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {0, 0});
        visited[0][0] = 1;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] == 1 && visited[nx][ny] == 0) {
                    queue.offer(new int[] {nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        
    }
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        visited = new int[n][m];
        
        if (maps[0][0] == 0) return -1;

        bfs(maps);
        
        int answer = visited[n-1][m-1];
        if(answer == 0) {
            answer = -1;
        }
        return answer;
    }
}