import java.util.*;

class Solution {
    
    static int n, m;
    static boolean[][] visited;
    static int[][] dist;
    
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public int bfs(int x, int y, int[][] maps) {
        ArrayDeque<int []> queue = new ArrayDeque<>();
        queue.offer(new int[]{x, y});
        
        visited[x][y] = true;
        dist[x][y] = 1;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int sx = cur[0];
            int sy = cur[1];
            
            // base
            if (sx == n - 1 && sy == m - 1) {
                return dist[sx][sy];
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + sx;
                int ny = dy[i] + sy;
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny] && maps[nx][ny] == 1) {
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                        dist[nx][ny] = dist[sx][sy] + 1;
                    }
                }
            }
        }
        
        return -1;
    }
    
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        
        visited = new boolean[n][m];
        dist = new int[n][m];

        return bfs(0, 0, maps);
    }
}