import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] cards = new int[N];
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(cards);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] targets = new int[M];
        for (int i = 0; i < M; i++) {
            targets[i] = Integer.parseInt(st.nextToken());

            bw.write(binarySearch(targets[i], cards) ? "1 " : "0 ");
            bw.flush();
        }
    
    }

    private static boolean binarySearch(int target, int[] cards) {
        int left = 0;
        int right = cards.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int val = cards[mid];

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
}   
