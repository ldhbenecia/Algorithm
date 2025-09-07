import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String n = br.readLine();
        int[] nums = new int[10];

        for (int i = 0; i < n.length(); i++) {
            int num = n.charAt(i) - '0';

            if (num == 6 || num == 9) {
                if (nums[6] <= nums[9]) {
                    nums[6]++;
                } else {
                    nums[9]++;
                }
            } else {
                nums[num]++;
            }
        }

        int result = 0;
        for (int c : nums) {
            if (c > result) result = c;
        }

        bw.write(String.valueOf(result));
        bw.flush();
    }
}
