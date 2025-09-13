import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void dfs(int x, int y, char color) {
        Deque<int[]> stack = new ArrayDeque<>();
        stack.add(new int[]{x, y});
        visited[x][y] = true;

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int cx = cur[0];
            int cy = cur[1];

            for (int d = 0; d < 4; d++) {
                int nx = dx[d] + cx;
                int ny = dy[d] + cy;

                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && graph[nx][ny] == color) {
                    stack.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
    }

    public static void dfsRG(int x, int y, char color) {
        Deque<int[]> stack = new ArrayDeque<>();
        stack.add(new int[]{x, y});
        visited[x][y] = true;

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int cx = cur[0];
            int cy = cur[1];

            for (int d = 0; d < 4; d++) {
                int nx = dx[d] + cx;
                int ny = dy[d] + cy;

                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]) {
                    if ((color == 'R' || color == 'G') && (graph[nx][ny] == 'R' || graph[nx][ny] == 'G')) {
                        stack.add(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    } else if (color == 'B' && graph[nx][ny] == 'B') {
                        stack.add(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    }   
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        graph = new char[n][n];
        for (int i = 0; i < n; i++) {
            graph[i] = br.readLine().toCharArray();
        }

        // 일반인
        visited = new boolean[n][n];
        int normal = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    dfs(i, j, graph[i][j]);
                    normal++;
                }
            }
        }

        // 적록색약
        visited = new boolean[n][n];
        int unnormal = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    dfsRG(i, j, graph[i][j]);
                    unnormal++;
                }
            }
        }

        bw.write(normal + " " + unnormal + "\n");
        bw.flush();
    }
}
