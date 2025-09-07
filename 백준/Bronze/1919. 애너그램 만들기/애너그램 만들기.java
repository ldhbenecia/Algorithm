import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String a = br.readLine();
        String b = br.readLine();

        char[] first = a.toCharArray();
        char[] second = b.toCharArray();
    
        Arrays.sort(first);
        Arrays.sort(second);

        int start = 0;
        int end = 0;
        int result = 0;

        // 두 문자열 중 하나가 끝까지 갈 때까지 비교, 정렬이 되어있으며 그 뒷부분은 다 카운팅해야하므로
        while (start < first.length && end < second.length) {
            if (first[start] == second[end]) {
                start++;
                end++;
            } else if (first[start] < second[end]) {
                result++;
                start++;
            } else {
                result++;
                end++;
            }
        }

        // 한 문자열의 끝을 찍었으니 그 뒤에 남은 부분은 전부 다른 문자임
        result += first.length - start;
        result += second.length - end;

        bw.write(String.valueOf(result));
        bw.flush();
    }
}
