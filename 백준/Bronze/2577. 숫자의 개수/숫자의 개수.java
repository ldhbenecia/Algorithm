import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());

        int temp = a * b * c;
        int[] dp = new int[10];

        String str = String.valueOf(temp);
        for (int i = 0; i < str.length(); i++) {
            int digit = str.charAt(i) - '0';
            dp[digit]++;
        }

        for (int i : dp) {
            bw.write(i + "\n");   
        }

        bw.flush();
        bw.close();
    }
}
