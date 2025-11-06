import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        long answer = 0;
        int[] cnt = new int[100001];

        while (left < n) {
            // right를 가능한만큼 확장 (중복 나오기 전까지), 0으로 초기화가 되어있고 방문하지 않은 것을 뜻함
            while(right < n && cnt[nums[right]] == 0) {
                cnt[nums[right]]++; // 방문 처리
                right++; // right 늘리기
            }

            // left 기준으로 다른 수 부분 배열 수
            // 2 5라면 2 2, 2 3, 2 4로 3개임
            answer += (right - left);

            // left 이동하며 제거
            cnt[nums[left]]--;
            left++;
        }

        bw.write(answer + "\n");
        bw.flush();
    }
}   
