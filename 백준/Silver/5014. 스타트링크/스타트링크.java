import java.io.*;
import java.util.*;

public class Main {

    static int F, S, G, U, D;
    static int[] visited;

    public static int bfs() {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(S);
        visited[S] = 0;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            // base
            if (cur == G) {
                return visited[cur];
            }

            int up = cur + U;
            if (0 < up && up <= F && visited[up] == -1) {
                visited[up] = visited[cur] + 1;
                queue.offer(up);
            }

            int down = cur - D;
            if (0 < down && down <= F && visited[down] == -1) {
                visited[down] = visited[cur] + 1;
                queue.offer(down);
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        F = Integer.parseInt(st.nextToken()); // 최고 층
        S = Integer.parseInt(st.nextToken()); // 시작 층
        G = Integer.parseInt(st.nextToken()); // 목표 층
        U = Integer.parseInt(st.nextToken()); // 위로 버튼
        D = Integer.parseInt(st.nextToken()); // 아래로 버튼

        visited = new int[F + 1];
        Arrays.fill(visited, -1);

        if (S == G) {
            bw.write(0 + "\n");
            bw.flush();
            return;
        }

        int result = bfs();
        if (result == - 1) {
            bw.write("use the stairs");
        } else {
            bw.write(result + "\n");
        }

        bw.flush();
    }
}   
