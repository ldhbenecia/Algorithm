import java.io.*;
import java.util.*;

public class Main {
    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Map<Integer, Integer> freq = new HashMap<>();

        for (int i = 0; i < N; i++) {
            int x =  Integer.parseInt(st.nextToken());
            freq.put(x, freq.getOrDefault(x, 0) + 1); // 존재하면 +1, 없으면 0
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) {
            int t = Integer.parseInt(st.nextToken());
            int count = freq.getOrDefault(t, 0);
            bw.write(count + " ");
        }

        bw.flush();
    }
}   
