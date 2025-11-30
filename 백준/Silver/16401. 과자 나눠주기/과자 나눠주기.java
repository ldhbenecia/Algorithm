import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        
        int[] snacks = new int[N];
        st = new StringTokenizer(br.readLine());
        int maxLen = 0;
        for (int i = 0; i < N; i++) {
            snacks[i] = Integer.parseInt(st.nextToken());
            if (snacks[i] > maxLen) maxLen = snacks[i];
        }

        // 과자 길이가 10억개까지 되므로 시간복잡도가 log단위로 떨어져야함
        // 입력 조건에서 오름차순으로 정렬은 보장되어있음
        // 탐색 알고리즘 사용 필요
        int left = 1;
        int right = maxLen;
        int result = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            long pieces = 0;
            for (int s : snacks) {
                pieces += (s / mid);
                if (pieces >= M) break;
            }

            if (pieces >= M) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
