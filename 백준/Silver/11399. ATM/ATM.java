import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int p[] = new int[n];
        st = new StringTokenizer(br.readLine());
                for (int i = 0; i < n; i++) {
            p[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(p);

        int temp = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            temp += p[i];
            sum += temp;
        }

        bw.write(sum + "\n");
        bw.flush();
    }
}   
