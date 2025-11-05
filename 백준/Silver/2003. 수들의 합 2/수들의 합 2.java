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
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        
        int result = 0;
        int left = 0;
        int right = 0;
        int sum = 0;

        while (true) {
            if (sum >= M) {
                if (sum == M) {
                    result++;
                }
                if (left < N) {
                    sum -= A[left];
                    left++;
                } else {
                    break;
                }
            } else { // sum < M
                if (right < N) {
                    sum += A[right];
                    right++;
                } else {
                    break;
                }
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
