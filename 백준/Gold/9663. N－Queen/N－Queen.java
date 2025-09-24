import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int result = 0;
    static int[] queens;

    public static boolean check(int current_row, int current_col) {
        for (int prev_row = 0; prev_row < current_row; prev_row++) {
            if (queens[prev_row] == current_col || Math.abs(current_row - prev_row) == Math.abs(current_col - queens[prev_row]))
            return false;
        }
        return true;

        // current_row: 1, current_col: 0 ~ 3
        // 이전 퀸: (2, 3)
        // 현재 퀸: (4, 5)
        // 행 차이: abs(4 - 2) = 2
        // 열 차이: abs(5 - 3) = 2
        // Math.abs(current_row - prev_row) -> 놓으려는 행과 이전 퀸의 행의 차이
        // Math.abs(current_col - queens[prev_row]) -> 놓으려는 열과 이전 퀸의 열의 차이


        /*
         * (1, 1)을 기준으로 대각
         * (0, 0) = abs(1 - 0) == abs(1 - 0) = 1
         * (2, 2) = abs(1 - 2) == abs(1 - 2) = 1
         * (0, 2) = abs(1 - 0) == abs(1 - 2) = 1
         */
    }

    public static void backtracking(int row) {
        // base
        if (row == n) {
            result += 1;
            return;
        }
        
        for (int col = 0; col < n; col++) {
            if (check(row, col)) {
                queens[row] = col;
                backtracking(row + 1);
            } 
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        queens = new int[n];

        backtracking(0);

        bw.write(result + "\n");
        bw.flush();
    }
}
