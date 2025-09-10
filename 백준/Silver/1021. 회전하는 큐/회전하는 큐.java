import java.io.*;
import java.util.*;

public class Main {

    public static int calculate(Deque<Integer> queue, int target) {
        int cnt = 0;
        int idx = 0;
        for (int num : queue) {
            if (num == target) break;
            idx++;
        }

        if (idx < queue.size() - idx) {
            for (int i = 0; i < idx; i++) {
                queue.addLast(queue.pollFirst());
                cnt++;
            }
        } else {
            for (int i = 0; i < queue.size() - idx; i++) {
                queue.addFirst(queue.pollLast());
                cnt++;
            }
        }

        queue.pollFirst();
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] position = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            position[i] = Integer.parseInt(st.nextToken());
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }
        int result = 0;

        for (int pos : position) {
            result += calculate(queue, pos);
        }

        bw.write(result + "\n");
        bw.flush();
    }
}
