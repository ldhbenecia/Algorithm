import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        // LinkedHashSet은 중복 허용 안하고 기존 값을 제거하고 뒤로 이동시킴, O(1)
        // List는 중복 허용, 삭제/이동 O(N)
        LinkedHashSet<String> waitlist = new LinkedHashSet<>();

        for (int i = 0; i < L; i++) {
            String id = br.readLine();

            if (waitlist.contains(id)) {
                waitlist.remove(id);
            }
            waitlist.add(id);
        }

        int cnt = 0;
        for (String id : waitlist) {
            if (cnt >= K) break;
            bw.write(id + "\n");
            cnt++;
        }

        bw.flush();
    }
}   
