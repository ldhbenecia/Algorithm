import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Deque<Integer> stack = new ArrayDeque<>();
        StringBuffer sb = new StringBuffer();

        int num = 1;
        boolean possible = true;

        for (int target : arr) {
            // target에 도달할 때 까지 push
            while (num <= target) {
                stack.push(num++);
                sb.append("+\n");
            }

            // 도달했으면 pop (top에 target 오면 빼고 - 추가)
            if (!stack.isEmpty() && stack.peek() == target) {
                stack.pop();
                sb.append("-\n");
            } else {
                possible = false;
                break;
            }
        }

        if (possible) {
            bw.write(sb.toString());
        } else {
            bw.write("NO\n");
        }

        bw.flush();
    }
}
