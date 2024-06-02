import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

  private static int n, m;
  private static int[] nums;
  private static int[] result;
  private static StringBuilder sb;

  public static void backtracking(int length) {

    // base 조건: m만큼 수열을 생성하면 출력
    if (length == m) {
      for (int i = 0; i < m; i++) {
        sb.append(result[i]).append(" ");
      }
      sb.append("\n");
      return;
    }

    for (int i = 0; i < n; i++) {
      if (i > 0 && nums[i - 1] == nums[i]) {
        continue;
      }
      result[length] = nums[i];
      backtracking(length + 1);
    }
  }
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    nums = new int[n];
    result = new int[m];
    sb = new StringBuilder();
    
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      nums[i] = (Integer.parseInt(st.nextToken()));
    }
    Arrays.sort(nums);
    backtracking(0);
    System.out.print(sb.toString());
  }
}
