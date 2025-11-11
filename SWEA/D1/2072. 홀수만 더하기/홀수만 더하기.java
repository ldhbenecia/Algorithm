import java.io.*;
import java.util.*;
import java.io.FileInputStream;

class Solution {
	public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int i = 1; i <= T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int sum = 0;
            
             for (int j = 0; j < 10; j++) {
                 int x = Integer.parseInt(st.nextToken());
                 if (x % 2 != 0) {
                 	sum += x;
                 }
             }
            System.out.println("#" + i + " " + sum);

        }      
    }
}