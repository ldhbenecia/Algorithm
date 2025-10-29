import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        int M = Integer.parseInt(br.readLine());
        int[] targets = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            targets[i] = Integer.parseInt(st.nextToken());
        }
        
        for (int t: targets) {
            int left = 0;
            int right = N - 1;
            boolean isFound = false;

            while (left <= right) {
                int mid = (left + right) / 2;

                if (A[mid] == t) {
                    isFound = true;
                    break;
                } else if (A[mid] < t) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }   

            if (isFound == true) {
                bw.write(1 + "\n");
            } else {
                bw.write(0 + "\n");
            }
        }
        
        bw.flush();
    }
}   
