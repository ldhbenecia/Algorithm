import java.io.*;
import java.util.*;

public class Main {
    
    static int n, m;
    static int[][] graph;
    static final int[] dx = {-1 , 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static class State {
        int x;
        int y;
        int broken; // 0: 안 부심, 1: 부심

        State(int x, int y, int broken) {
            this.x = x;
            this.y = y;
            this.broken = broken;
        }
    }

    private static int bfs() {
        ArrayDeque<State> queue = new ArrayDeque<>();
        boolean[][][] visited = new boolean[n][m][2];
        int[][][] dist = new int[n][m][2];

        visited[0][0][0] = true;
        dist[0][0][0] = 1;
        queue.offer(new State(0, 0, 0));

        while (!queue.isEmpty()) {
            State cur = queue.poll();
            
            // base
            if (cur.x == n - 1 && cur.y == m - 1) {
                return dist[cur.x][cur.y][cur.broken];
            }

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + cur.x;
                int ny = dy[i] + cur.y;

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    // 빈 칸: 현재 broken 유지, 방문 체킹 후 이동
                    if (graph[nx][ny] == 0) {
                        if (!visited[nx][ny][cur.broken]) {
                            visited[nx][ny][cur.broken] = true;
                            dist[nx][ny][cur.broken] = dist[cur.x][cur.y][cur.broken] + 1;
                            queue.offer(new State(nx, ny, cur.broken));
                        }
                    } else { // 벽
                        // 벽 아직 부신 적 없으면 이 벽을 부시고 상태 1로 변환
                        if (cur.broken == 0 && !visited[nx][ny][1]) {
                            visited[nx][ny][1] = true;
                            dist[nx][ny][1] = dist[cur.x][cur.y][cur.broken] + 1;
                            queue.offer(new State(nx, ny, 1));
                        }
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

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        int result = bfs();
        bw.write(result + "\n");
        bw.flush();
    }
}   
