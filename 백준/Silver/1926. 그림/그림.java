import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static int bfs(int sx, int sy) {
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{sx, sy});
        visited[sx][sy] = true;
        int area = 1;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if ((0 <= nx && nx < n) && (0 <= ny && ny < m)) {
                    if (!visited[nx][ny] && graph[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                        area++;
                    }
                }
            }
        }

        return area;
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
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int cnt = 0;
        int result = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    cnt++;
                    result = Math.max(result, bfs(i, j));
                }
            }
        }

        bw.write(cnt + "\n");
        bw.write(result + "\n");
        bw.flush();
    }
}   
