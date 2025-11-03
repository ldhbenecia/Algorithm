import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(A);

        // 두 수의 차가 3보다 큰 값 중에 가장 작은 값
        // 1 5, 1 3, 5 3
        // 4, 2, 2 => 3보다 큰 수 중에 4가 가장 크니까 4가 답

        // 입력 범위 값이 커서 n^2 이상의 시간복잡도가 나오면 안됨
        // 탐색 알고리즘 사용

        int left = 0;
        int right = 0;
        int answer = Integer.MAX_VALUE;

        while (right < N && left <= right) {
            int diff = A[right] - A[left];

            if (diff >= M) {
                if (diff < answer) {
                    answer = diff;
                }
                left++; // 동기화 후 다른 가능성을 두고 추가 탐색, 더 작은 차이가 있는지 확인을 위해 left++
            } else {
                right++; // 차이가 부족함, right++
            }
        }

        bw.write(answer + "\n");
        bw.flush();
    }
}   
