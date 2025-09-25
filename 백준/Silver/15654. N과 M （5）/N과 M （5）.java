import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] nums;
    static List<Integer> temp = new ArrayList<>();
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void backtracking(int depth) throws IOException {
        // base
        if (depth == m) {
            for (int i : temp) {
                bw.write(i + " ");
            }
            bw.write("\n");
            return;
        }

        for (int i = 0; i < n; i++) {
            if (temp.contains(nums[i])) continue;
            temp.add(nums[i]);
            backtracking(depth + 1);
            temp.remove(temp.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken()); 

        nums = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        Arrays.sort(nums);
        
        backtracking(0);

        bw.flush();
    }
}   
