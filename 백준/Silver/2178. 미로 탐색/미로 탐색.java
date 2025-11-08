import java.io.*;
import java.util.*;

public class Main {
    
    static int n, m;
    static int[][] graph;
    static boolean[][] visited;
    static final int[] dx = {-1 , 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    private static int bfs(int sx, int sy) {
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        visited[sx][sy] = true;
        
        queue.offer(new int[]{sx, sy});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];

            // base
            if (x == n - 1 && y == m - 1) {
                return graph[n-1][m-1];
            }

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                if ((0 <= nx && nx < n) && (0 <= ny && ny < m)) {
                    if (visited[nx][ny] == false && graph[nx][ny] == 1) {
                        graph[nx][ny] = graph[x][y] + 1;
                        visited[nx][ny] = true;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        int result = bfs(0, 0);
        bw.write(result + "\n");
        bw.flush();
    }
}   
