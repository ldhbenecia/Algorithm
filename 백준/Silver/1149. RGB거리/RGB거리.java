import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N + 1][3]; // 1번 집부터 시작, RGB 3개

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            // 색상이 앞 뒤로 달라야함
            // 각각의 색깔일 때 이전과 이후의 빨강 초록 중에 작은 값을 찾아 더함
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + r; // i번째 집이 빨강일 때
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + g; // i번째 집이 초록일 때
            dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + b; // i번째 집이 파랑일 때
        }

        bw.write(Math.min(dp[N][0], Math.min(dp[N][1], dp[N][2])) + "\n");
        bw.flush();
    }
}   
