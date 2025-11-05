import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        
        // 주어진 N을 소수의 합으로 나타낼 수 있는가
        // 몇 개 나타낼 수 있는가


        // N까지의 소수 배열 구하기
        // 에라토스테네스의 체 -> 2부터 루트 K까지 탐색
        // 2부터 k/2까지 나눴을 때 나눠지는 숫자가 없으면 소수
        ArrayList<Integer> primes = new ArrayList<>();
        for (int i = 2; i < N + 1; i++) {
            boolean isPrime = true;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                primes.add(i);
            }
        }

        // 시간 초과
        // int result = 0;
        // for (int i = 0; i < prime.size(); i++) {
        //     int temp  = 0;
        //     for (int j = i; j < prime.size(); j++) {
        //         temp += prime.get(j);
        //         if (temp == N) {
        //             result++;
        //             break;
        //         }
        //     }
        // }

        // 탐색에서 시간초과가 났으므로 투포인터 사용
        int result = 0;
        int left = 0;
        int right = 0;
        int sum = 0;
        while (true) {
            if (sum >= N) {
                if (sum == N) {
                    result++;
                }
                
                // 더 적은 합 탐색
                if (left < primes.size()) {
                    sum -= primes.get(left);
                    left++;
                } else {
                    break;
                }
            } else { // sum < N
                if (right < primes.size()) {
                    sum += primes.get(right);
                    right++;
                } else {
                    break;
                }
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }
}   
