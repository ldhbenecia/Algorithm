import java.io.*;
import java.util.*;

public class Main {

    private static int[] bfs(int start, List<List<Integer>> graph, int N) {
        int[] dist = new int[N + 1];
        Arrays.fill(dist, -1);

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        dist[start] = 0;
        queue.offer(start);

        while (!queue.isEmpty()) {
            int v = queue.poll();

            for (int nx : graph.get(v))
                if (dist[nx] == -1) {
                    dist[nx] = dist[v] + 1;
                    queue.offer(nx);
                }
        }

        return dist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            graph.get(A).add(B);
            graph.get(B).add(A);
        }

        int bestSum = Integer.MAX_VALUE;
        int bestNode = 1;

        // 각 노드에서 BFS -> 거리 합 계산
        for (int i = 1; i <= N; i++) {
            int[] dist = bfs(i, graph, N);

            int total = 0;
            for (int v = 1; v <= N; v++) {
                total += dist[v];
            }

            if (total < bestSum) {
                bestSum = total;
                bestNode = i;
            }
        }

        bw.write(bestNode + "\n");
        bw.flush();
    }
}   
