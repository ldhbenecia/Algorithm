import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] W = new int[N + 1];
		int[] V = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
			V[i] = Integer.parseInt(st.nextToken());
        }

        // dp[i][j]: 앞의 i개 물건을 가지고 배낭 용량 j에서 얻을 수 있는 최대 가치
        int[][] dp = new int[N + 1][K + 1];

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                // 현재 물건 i의 무게 W[i]를 용량 j에 담을 수 없는 경우: i번째 물건을 안 담은 값 유지
                if (W[i] > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    // 담을 수 있는 경우: (i번째 물건을 안 담는 경우) vs (담는 경우) 중 최대
                    // 안 담는 경우: dp[i - 1][j]
                    // 담는 경우: dp[i - 1][j - W[i]] + V[i]
                    // j - W[i]는 i번째 물건을 담고 남는 용량이며, V[i]는 그 물건의 가치
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i]);
                }
            }
        }

        bw.write(dp[N][K] + "\n");
        bw.flush();
    }
}   
