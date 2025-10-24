import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int a[] = new int[n];
        st = new StringTokenizer(br.readLine());
                for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);

        int b[] = new int[n];
        st = new StringTokenizer(br.readLine());
    
        for (int i = 0; i < n; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(b);

        int result = 0;
        for (int i = 0; i < n; i++) {
            result += a[i] * b[n - 1 - i];
        }
        
        bw.write(result + "\n");
        bw.flush();
    }
}   
