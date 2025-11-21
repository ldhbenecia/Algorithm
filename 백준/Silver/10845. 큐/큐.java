import java.io.*;
import java.util.*;

public class Main {



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        ArrayDeque<Integer> queue = new ArrayDeque<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            StringTokenizer st = new StringTokenizer(line);
            String command = st.nextToken();

            if (command.equals("push")) {
                int X = Integer.parseInt(st.nextToken());
                queue.offer(X);
            } else if (command.equals("front")) {
                if (!queue.isEmpty()) {
                    bw.write(queue.getFirst() + "\n");
                } else {
                    bw.write(-1 + "\n");
                }
            } else if (command.equals("back")) {
                if (!queue.isEmpty()) {
                    bw.write(queue.getLast() + "\n");
                } else {
                    bw.write(-1 + "\n");
                }
            } else if (command.equals("size")) {
                bw.write(queue.size() + "\n");
            } else if (command.equals("empty")) {
                if (!queue.isEmpty()) {
                    bw.write(0 + "\n");
                } else {
                    bw.write(1 + "\n");
                }
            } else if (command.equals("pop")) {
                if (!queue.isEmpty()) {
                    bw.write(queue.pollFirst() + "\n");
                } else {
                    bw.write(-1 + "\n");
                }
            }

            bw.flush();
        }
    }
}   
