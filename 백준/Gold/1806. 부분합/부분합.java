import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // S 입력 범위 100,000,000
        // 시간 제한 Java 1초
        // n^2 불가능, N 이하로 연산

        // DP(누적합), 투포인터 둘 다 가능할 것 같음
        int len = Integer.MAX_VALUE;
        int left = 0;
        int right = 0;
        int sum = 0;
        while (true) {
            if (sum >= S) {
                len = Math.min(len, right - left);
                sum -= nums[left++];
            } else {
                if (right == N) {
                    break;
                }
                sum += nums[right++];
            }
        }

        bw.write(len == Integer.MAX_VALUE ? "0\n" : (len + "\n"));
        bw.flush();
    }
}   
