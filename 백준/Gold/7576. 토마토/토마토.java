import java.io.*;
import java.util.*;

public class Main {
    
    static int n, m;
    static int[][] graph;
    static final int[] dx = {-1 , 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    private static int bfs() {
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        
        // 익은 토마토를 큐에 모두 삽입
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                if ((0 <= nx && nx < n) && (0 <= ny && ny < m)) {
                    if (graph[nx][ny] == 0) {
                        graph[nx][ny] = graph[x][y] + 1;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
        }

        int maxVal = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    return -1;
                }
                maxVal = Math.max(maxVal, graph[i][j]);
            }
        }

        return maxVal - 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result = bfs();
        bw.write(result + "\n");
        bw.flush();
    }
}   
