import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        // DP
        // 1 -> 1 : 1개
        // 2 -> 1+1, 2 : 2개
        // 3 -> 1+1+1, 1+2, 2+1, 3 : 4개
        // 4 -> 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1, 4 : 7개
        // 5 -> 13개

        // 4 -> 1,2,3 -> 1+2+4 = 7개
        // 5 -> 2,3,4 -> 2+4+7 = 13개
        // 점화식: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        int T = Integer.parseInt(br.readLine());
        int[] dp = new int[11]; // 입력 조건에 n은 양수이며 11보다 작다.
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i < 11; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            bw.write(dp[n] + "\n");
        }
        bw.flush();
    }
}   
