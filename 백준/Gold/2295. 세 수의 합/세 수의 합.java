import java.io.*;
import java.util.*;

public class Main {

    private static boolean binarySearch(ArrayList<Integer> arr, int target) {
        int left = 0;
        int right = arr.size() - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            
            int val = arr.get(mid);
            if (val == target) {
                return true;
            } else if (val < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine()); // 1,000이므로 2중 for문까지 가능
        int[] U = new int[N];
        for (int i = 0; i < N; i++) {
            U[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(U);

        ArrayList<Integer> sum = new ArrayList<>();
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                sum.add(U[x] + U[y]);
            }
        }
        Collections.sort(sum);

        // 가장 큰 k부터 내려가며 k = x + y + z 성립 여부 검사
        for (int k = N - 1; k >= 0; k--) {
            int d = U[k]; // 가장 큰 수 d

            // z를 순회하며 k - z가 두 수의 합인지 확인
            for (int z = 0; z < N; z++) {
                int target = d - U[z];
                
                if (binarySearch(sum, target)) {
                    bw.write(d + "\n");
                    bw.flush();
                    return;
                }
            }
        }

        bw.write("0");
        bw.flush();
    }
}   
