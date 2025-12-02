import java.io.*;
import java.util.*;

public class Main {

    private static final int INF = 1_000_000; 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        int n = Integer.parseInt(br.readLine());
        
        // 트리로 연결
        // root = 1
        // 회원번호 두 개씩 연결
        // 각 원소당 몇개가 연결되어있는지를 체크해서 등급 매기기

        // 그래프 탐색을 해서 이어진 개수가 몇개인지 체크
        // 플루이드 워셜 가능

        int[][] dist = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // base
            if (a == -1 && b == -1) break;

            dist[a][b] = 1;
            dist[b][a] = 1;
        }

        // 플루이드 워셜
        // 중간 정점 k를 통해 i->j로 가는 경로가 더 짧으면 갱신
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                if (dist[i][k] == INF) continue; // i->k가 끊겨 있으면 스킵
                for (int j = 1; j <= n; j++) {
                    if (dist[k][j] == INF) continue; // k->j가 끊겨 있으면 스킵

                    // i->j를 하며 k를 거쳐가는 경로가 더 짧을 경우 갱신
                    if ((dist[i][k] + dist[k][j]) < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        // 회원 점수 계산: 가장 멀리 있는 회원까지의 거리
        int[] score = new int[n + 1];
        int minScore = INF;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                score[i] = Math.max(score[i], dist[i][j]);
            }
            minScore = Math.min(minScore, score[i]);
        }

        // 오름차순으로 후보 저장
        List<Integer> candidates = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (score[i] == minScore) {
                candidates.add(i);
            }
        }

        bw.write(minScore + " " + candidates.size() + "\n");
        for (int i = 0; i < candidates.size(); i++) {
            bw.write(String.valueOf(candidates.get(i)));
            if (i + 1 < candidates.size()) bw.write(" ");
        }
        bw.flush();
    }
}   
