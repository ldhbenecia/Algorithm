import java.io.*;
import java.util.*;

public class Main {

    private static final int INF = 1_000_000; 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        int n = Integer.parseInt(br.readLine());
        int[] stairs = new int[n];
        for (int i = 0; i < n; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        if (n == 1) {
            bw.write(stairs[0] + "\n");
            bw.flush();
            return;
        }

        if (n == 2) {
            bw.write(stairs[0] + stairs[1] + "\n");
            bw.flush();
            return;
        }

        int[] dp = new int[n];
        dp[0] = stairs[0];
        dp[1] = stairs[0] + stairs[1]; // 두번째 계단 밟았을 경우
        dp[2] = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2]); // 세번째 계단 밟았을 경우

        for (int i = 3; i < n; i++) {
            dp[i] = Math.max(
                dp[i - 2] + stairs[i], // 두 계단 점프
                dp[i - 3] + stairs[i - 1] + stairs[i] // 두 계단 후 한 계단 점프
            );
        }

        bw.write(dp[n - 1] + "\n");
        bw.flush();
    }
}   
