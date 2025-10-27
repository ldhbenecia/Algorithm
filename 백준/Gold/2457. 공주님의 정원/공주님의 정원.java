import java.io.*;
import java.util.*;

public class Main {

    static class Flower {
        int start, end;

        public Flower(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        Flower[] flowers = new Flower[n];
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int startMonth = Integer.parseInt(st.nextToken());
            int startDay = Integer.parseInt(st.nextToken());
            int endMonth = Integer.parseInt(st.nextToken());
            int endDay = Integer.parseInt(st.nextToken());

            // 시작 일자 MMDD로 변환
            int start = startMonth * 100 + startDay;
            int end = endMonth * 100 + endDay;
            flowers[i] = new Flower(start, end);
        }

        // 시작일 기준 오름차순 정렬, 시작일이 같을 경우 내림차순 정렬
        Arrays.sort(flowers, (f1, f2) -> {
            if (f1.start == f2.start) return f2.end - f1.end;
            return f1.start - f2.start;
        });

        // 조건 0301 ~ 1130
        final int requireStart = 301; // 3월 1일부터 꽃이 펴서 볼 수 있음
        final int requireEnd = 1201; // 이 날부터 졌으므로 1130까지 펴있음(볼 수 있음)

        int count = 0; // 선택한 꽃 개수
        int idx = 0; // 스캔 포인터
        int current = requireStart; // 서칭 시작 지점을 현재 값으로 설정(301)
        int bestExtend = current; // 검사전은 현재 값으로 설정(301)

        while (current < requireEnd) {
            boolean isFind = false;

            // 조건: 입력받은 꽃의 개화 시작일자가 3월 1일보다 빨리 펴야함
            // 조건: 입력받은 꽃이 지는 일자가 가장 긴 시기를 택하여 동기화 후 선택
            while (idx < n && flowers[idx].start <= current) {
                // ROUND 1
                // 1월 1일 ~ 6월 30일의 경우 1월 1일이 3월 1일보다 전이니 조건 성립
                // 6월 30일의 경우 현재 초기값 3월 1일보다 크므로 꽃을 볼 수 있음 선택
                // bestExtend 630으로 동기화

                // 1월 1일 ~ 5월 31일의 경우 while문 조건은 성립하나
                // bestExtend가 630 > 531이므로 if 조건에 성립하지않아서 pass

                // 여기까지 while 연산 후 current = 630으로 동기화
                // 1월 1일 ~ 6월 30일은 선택하고 5월 31일까지는 패스했으므로
                // 6월 30일까지 꽃을 볼 수 있는 경우는 보장되었음
                // ------------------------------------------------

                // ROUND 2
                // 5월 15일 ~ 8월 31일의 경우 current 630보다 전이니 조건 성립
                // 8월 31일의 경우 current 630보다 크므로 꽃을 볼 수 있음 선택
                // bestExtend 831로 동기화

                // 6월 10일 ~ 12 10일의 경우 current 831보다 전이니 조건 성립
                // 12월 10일의 경우 bestExtend 831보다 크므로
                // bestExtend 1210으로 동기화, 선택
                
                // ROUND 2에서는 515~831, 610~1210이 둘 다 후보에 올랐음
                // 여기서 610~1210이 선택되었음
                // while 연산 후 current = bestExtend로 current 1210으로 동기화
                // current 1210 > 1201보다 크므로 연산 종료

                // 최종적으로 획득한 꽃
                // ROUND1 101 ~ 630
                // ROUND2 610 ~ 1210
                // 최종적으로 연속적으로 이어지기 때문에 정답은 2
                if (flowers[idx].end > bestExtend) {
                    bestExtend = flowers[idx].end;
                    isFind = true;
                }
                idx++;
            }

            // 중간에 공백이 생겼을 경우 못 보는 경우가 생겨서 0 처리
            if (!isFind) {
                count = 0;
                break;
            }
            count++;
            current = bestExtend;
        }

        bw.write(count + "\n");
        bw.flush();
    }
}   
