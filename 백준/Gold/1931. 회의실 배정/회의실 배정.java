import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int n = Integer.parseInt(br.readLine());

    int[][] times = new int[n][2];
    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      times[i][0] = Integer.parseInt(st.nextToken()); // 시작 시간
      times[i][1] = Integer.parseInt(st.nextToken()); // 종료 시간
    }

    // 종료 시간을 기준으로 정렬 (종료 시간이 같을 경우 시작 시간이 빠른 순으로 정렬)
    Arrays.sort(times, (a, b) -> {
      if (a[1] == b[1]) {
        return a[0] - b[0]; // 시작 시간 기준 정렬
      } else {
        return a[1] - b[1]; // 종료 시간 기준 정렬
      }
    });

    int result = 0;
    int prev = -1;
    for (int i = 0; i < n; i++) {
      if (prev <= times[i][0]) {
        prev = times[i][1];
        result++;
      }
    }

    System.out.println(result);
  }
}
