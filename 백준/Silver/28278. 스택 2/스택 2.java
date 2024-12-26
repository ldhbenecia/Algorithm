import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    StringTokenizer st;
    Stack<Integer> stack = new Stack<>();

    int n = Integer.parseInt(br.readLine());

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());

      switch(st.nextToken()) {
        case "1":
          stack.push(Integer.parseInt(st.nextToken()));
          break;

        case "2":
          if (stack.isEmpty()) {
            sb.append(-1).append("\n");
          } else {
            sb.append(stack.pop()).append("\n");
          }
          break;

        case "3":
          sb.append(stack.size()).append("\n");
          break;

        case "4":
          sb.append(stack.isEmpty() ? "1\n" : "0\n");
          break;

        case "5":
          if (stack.isEmpty()) {
            sb.append(-1).append("\n");
          } else {
            sb.append(stack.peek()).append("\n");
          }
          break;
      }
    }

    System.out.print(sb.toString());
  }
}
