import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());

    
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            String b = st.nextToken(); 

            if (a.length() != b.length()) {
                bw.write("Impossible\n");
                continue;
            }

            char[] first = a.toCharArray();
            char[] second = b.toCharArray();

            Arrays.sort(first);
            Arrays.sort(second);

            if (Arrays.equals(first, second)) {
                bw.write("Possible\n");
            } else {
                bw.write("Impossible\n");
            }
        }

        bw.flush();
    }
}
