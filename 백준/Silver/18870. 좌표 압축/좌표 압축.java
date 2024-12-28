import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    // 첫 번째 줄에서 좌표 개수 입력
    int n = Integer.parseInt(br.readLine());

    // 두 번째 줄에서 좌표 입력
    int[] nums = new int[n];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      nums[i] = Integer.parseInt(st.nextToken());
    }

    // 정렬된 배열 생성 및 정렬
    int[] sortedNums = nums.clone();
    Arrays.sort(sortedNums);

    // 좌표 압축을 위한 HashMap 생성
    HashMap<Integer, Integer> hashMap = new HashMap<>();
    int rank = 0;
    for (int num : sortedNums) {
      if (!hashMap.containsKey(num)) {
        hashMap.put(num, rank++);
      }
    }

    StringBuilder sb = new StringBuilder();
    for (int num : nums) {
      sb.append(hashMap.get(num)).append(" ");
    }

    System.out.println(sb);
  }
}
