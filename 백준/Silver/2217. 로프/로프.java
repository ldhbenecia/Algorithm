import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            weights[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(weights);

        int result = 0;
        for (int i = 0; i < n; i++) {
            int possible = weights[i] * (n - i);
            if (result < possible) {
                result = possible;
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
