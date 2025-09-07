import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] students = new int[2][6];
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int grade = Integer.parseInt(st.nextToken());
            students[gender][grade-1]++; // 학년별 학생 수 카운팅
        }

        int result = 0;
        for (int g = 0; g < 2; g++) {
            for (int gr = 0; gr < 6; gr++) {
                result += (students[g][gr] + k - 1) / k;
            }
        }

        bw.write(String.valueOf(result));
        bw.flush();
    }
}
