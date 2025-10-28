import java.io.*;
import java.util.*;

public class Main {

    private static int sumByPlus(String s) {
        StringTokenizer plusTokens = new StringTokenizer(s, "+");
        int sum = 0;

        while(plusTokens.hasMoreTokens()) {
            sum += Integer.parseInt(plusTokens.nextToken());
        }

        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String expr = br.readLine();

        // - 기준으로 분리
        StringTokenizer minusTokens = new StringTokenizer(expr, "-");
        int result = 0;
        boolean isFirstGroup = true;

        // 55 - 50 + 40 -> +45
        // 55 - (50 + 40) -> -35
        // - 연산자 이후의 값들을 괄호로 묶어어 함

        // 10 + 20 + 30 - 40 + 50 - 60 + 70
        // 60 - 90 - 130 -> -160
        // - 기준으로 분리를 하였기 때문에 ["10+20+30", "40+50", "60+70"]
        // minusTokens.nextTokens()를 하면 10+20+30 부터 나옴

        // 각 그룹을 + 기준으로 합산
        while(minusTokens.hasMoreTokens()) {
            String group = minusTokens.nextToken();
            int groupSum = sumByPlus(group); // 그룹 내 + 합산

            // 첫 그룹은 더하고, 이후 그룹 빼기
            if (isFirstGroup) {
                result += groupSum;
                isFirstGroup = false;
            } else {
                result -= groupSum;
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
