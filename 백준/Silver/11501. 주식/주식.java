import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] price = new int[n];

            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                price[j] = Integer.parseInt(st.nextToken());
            }
    

            // 날 수: 3, 주가: 10, 6, 7
            // 주가는 계속 감소하기에 최대 이익: 0
            // 3, 5, 9일 경우 처음 두 날에 하나씩 사고 마지막 날에 다 팔면
            // 최대 이익: 10
            // 3원에 1개, 5원에 1개 구매 = 구매비용 8월
            // 마지막날인 9원에 2개 판매 = 판매비용 18
            // 판매비용 - 구매비용 = 10

            // 1 1 3 1 2
            // 1원에 구매, 1원에 구매, 3원일때 2개 판매 -> 6 - 2 = 4원
            // 1원에 구매, 2원일때 1개 판매 -> 2 - 1 = 1
            // 4 + 1 = 5원

            // 고점을 기준으로 차익을 계산하려면 뒤에서부터 봐야한다.
            // 팔 날은 항상 오늘 이후의 가격들 중 최댓값

            // 1 1 3 1 2
            // 1. max price 2
            // 2. 1은 2보다 작음, 매수하고 2원에 판매했다면 차익 2 - 1 = 1
            // 3. 3은 2보다 큼, 고점 3으로 수정 (파는 날)
            // 4. 1은 3보다 작음, 매수하고 3원에 팔았다고 가정하면 이익 3 - 1 = 2
            // 5. 위와 같음, 3 - 1 = 2
            // 6. 1 + 2 + 2 = 5

            long result = 0;
            int maxPrice = 0;

            for (int p = n - 1; p >= 0; p--) {
                if (price[p] >= maxPrice) {
                    maxPrice = price[p]; // 고점을 발견하면 매도 날 갱신
                } else {
                    result += maxPrice - price[p];
                }
            }

            bw.write(result + "\n");
            bw.flush();
        }   
    }
}   
