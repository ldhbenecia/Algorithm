import java.io.*;
import java.util.*;

public class Main {

  public static int calculateChanges(String[] board, int startX, int startY) {
    String[] patterns = {"WBWBWBWB", "BWBWBWBW"};
    int count1 = 0; // 첫 번째 패턴 기준 변경 수
    int count2 = 0; // 두 번째 패턴 기준 변경 수

    for (int i = 0; i < 8; i++) {
      int row = startX + i;
      for (int j = 0; j < 8; j++) {
        int col = startY + j;
        char current = board[row].charAt(col);
        
        if (current != patterns[i % 2].charAt(j)) {
          count1++;
        }

        if (current != patterns[(i + 1) % 2].charAt(j)) {
          count2++;
        }
      }
    }

    // 흰색으로 시작 혹은 검정색으로 시작한 체스판으로 비교한 값 중 최소 변경 값 반환
    return Math.min(count1, count2);
  }

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    String[] board = new String[n];
    for (int i = 0; i < n; i++) {
      board[i] = br.readLine();
    }

    int result = Integer.MAX_VALUE; // 다시 칠해야 하는 정사각형 개수 최솟값

    for (int i = 0; i <= n - 8; i++) {
      for (int j = 0; j <= m - 8; j++) {
        result = Math.min(result, calculateChanges(board, i, j));
      }
    }

    bw.write(result + "\n");
    bw.flush();
    bw.close();
  }
}
