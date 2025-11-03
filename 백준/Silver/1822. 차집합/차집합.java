import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] A = new int[n];
        int[] B = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(B);

        // 이진 탐색 돌려서 없는 것만 따로 빼기
        ArrayList<Integer> result = new ArrayList<>();

        for (int t : A) {
            if (binarySearch(t, B)) {
                result.add(t);
            }
        }

        if (result.isEmpty()) {
            bw.write(0 + "\n");
            bw.flush();
            return;
        }

        bw.write(result.size() + "\n");
        for (int i = 0; i < result.size(); i++) {
            bw.write(result.get(i) + " ");
        }
        bw.flush();
    }

    private static boolean binarySearch(int target, int[] B) {
        int left = 0;
        int right = B.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int val = B[mid];

            if (val == target) {
                return false;
            } else if (val < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return true;
    }
}   
