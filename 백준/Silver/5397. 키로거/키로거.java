import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String key = br.readLine();

            Stack<Character> left = new Stack<>();
            Stack<Character> right = new Stack<>();

            for (char c : key.toCharArray()) {
                if (c == '<') {
                    if (!left.isEmpty()) {
                        right.push(left.pop());
                    }
                } else if (c == '>') {
                    if (!right.isEmpty()) {
                        left.push(right.pop());
                    }
                } else if (c == '-') {
                    if (!left.isEmpty()) {
                        left.pop();
                    }
                } else {
                    left.push(c);
                }
            }

            // 오른쪽에 값이 남아있다면 왼쪽으로 넣어주기
            while(!right.isEmpty()) {
                left.push(right.pop());
            }

            StringBuffer sb = new StringBuffer();
            for (char c : left) {
                sb.append(c);
            }

            bw.write(sb.toString() + "\n");
            bw.flush();
        }
    }
}
