import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] lan = new int[K];
        int maxLan = 0;
        for (int i = 0; i < K; i++) {
            lan[i] = Integer.parseInt(br.readLine());
            if (lan[i] > maxLan) maxLan = lan[i];
        }

        long left = 1;
        long right = maxLan;
        long result = 0;

        while (left <= right) {
            long mid = (left + right) / 2;

            long count = 0;
            for (int l : lan) {
                count += (l / mid);
            }

            if (count >= N) {
                // 더 많이 쪼갰을 경우 lan 길이를 늘려야함, N개 이상 만들 수 있기 때문에 더 만들 수 있는지 탐색
                result = mid; // 정답 동기화
                left = mid + 1;
            } else {
               // 적을 경우 lan을 더 잘게 쪼개야함
               right = mid - 1;
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
