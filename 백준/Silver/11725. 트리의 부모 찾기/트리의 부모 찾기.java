import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<ArrayList<Integer>> tree;
    static int parent[];

    private static void bfs(int root) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(root);
        parent[root] = -1;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            for (int nxt : tree.get(cur)) {
                if (parent[nxt] == 0) {
                    parent[nxt] = cur;
                    queue.add(nxt);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        tree = new ArrayList<>();
        parent = new int[N + 1];

        for (int i = 0; i <= N; i++) tree.add(new ArrayList<>());
        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            tree.get(a).add(b);
            tree.get(b).add(a);
        }

        bfs(1);

        for (int i = 2; i <= N; i++) {
            bw.write(parent[i] + "\n");
        }
        bw.flush();
    }
}   
