import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        int result = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (k == 0) break;
            if (coins[i] > k) continue;
    
            int use = k / coins[i];
            result += use;
            k -= coins[i] * use;
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
