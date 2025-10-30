import java.io.*;
import java.util.*;

public class Main {
    
    private static int lowerBound(int[] A, int value) {
        int left = 0, right = A.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (A[mid] >= value) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private static int upperBound(int[] A, int value) {
        int left = 0, right = A.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (A[mid] > value) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }


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
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int t = Integer.parseInt(st.nextToken());
            int count = upperBound(A, t) - lowerBound(A, t);
            bw.write(count + " ");
        }

        bw.flush();
    }
}   
