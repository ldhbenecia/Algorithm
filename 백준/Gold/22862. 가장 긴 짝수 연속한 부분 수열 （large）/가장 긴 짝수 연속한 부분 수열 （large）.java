import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] S = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            S[i] = Integer.parseInt(st.nextToken());
        }

        // 삭제 가능 횟수: K
        // 배열 S에서 최대 K번 원소를 삭제한 수열에서 짝수로 이루어져 있는
        // 연속한 부분 수열 중 가장 긴 길이 출력
        // 입력 범위 값으로 보아 n^2 불가능

        // 2번 삭제 가능
        // 1 2 3 4 5 6 7 8

        // 홀수를 제거
        // 1, 3제거 -> 245678 -> 짝수로 이루어져있는 최대 길이 24 2개
        // 1, 5제거 -> 234678 -> 46 2개
        // 1, 7제거 -> 234568 -> 68 2개
        // 3, 5제거 -> 124678 -> 246 3개
        // 3, 7제거 -> 124568 -> 24, 68 2개
        // 5, 7제거 -> 123468 -> 468 3개

        // 포인터 2개로 돌려서 S[left], S[right]에 나온 값이 홀수인지 판별 과정 필요
        // 슬라이딩 윈도우 [left, right] 윈도우 사이의 홀수 개수가 K개 이하
        // 윈도우에서 홀수 제거하고 남는 짝수 개수의 최대값 구하기

        int left = 0;
        int oddCount = 0;
        int result = 0;

        for (int right = 0; right < N; right++) {
            // 홀수 카운팅, 1 3 5 7
            if (S[right] % 2 != 0) {
                oddCount++;
            }

            // 제거할 홀수 카운트가 K개 초과하면 left를 늘리면서 줄임
            // 1 3 5가 oddCount로 3개가 되었을때 그때 left를 당겨서
            // [1, 2, 3, 4] -> [2, 3, 4, 5] -> [2, 3, 4, 5, 6] -> [2, 3, 4, 5, 6, 7] -> [4, 5, 6, 7]...
            while (oddCount > K && left <= right) {
                if (S[left] % 2 != 0) {
                    oddCount--;
                }
                left++;
            }

            int windowLen = right - left + 1;
            int evenCount = windowLen - oddCount;
            if (evenCount > result) {
                result = evenCount;
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
