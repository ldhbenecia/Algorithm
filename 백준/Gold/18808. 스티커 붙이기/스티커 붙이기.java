import java.io.*;
import java.util.*;

public class Main {

    static int[][] graph;
    static int N, M, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        graph = new int[N][M];

        // 모눈종이 스티커 붙이기
        for (int s = 0; s < K; s++) {
            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            // 스티커 등록
            int[][] sticker = new int[R][C];
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    sticker[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            attach(sticker);
        }

        // 스티커 붙이기 후 붙은 칸 수 출력 (result)
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == 1) {
                    result++;
                }
            }
        }

        bw.write(result + "\n");
        bw.flush();
    }

    // 0, 90, 180, 270도: 4번 회전하며 시도하고 붙이면 종료
    public static void attach(int[][] sticker) {
        for (int dir = 0; dir < 4; dir++) {
            int rows = sticker.length;
            int cols = sticker[0].length;
            boolean isAttach = false;

            // N: 5, M: 4, K: 4라고 했을 경우
            // R: 3, C: 3
            // 필요없는 줄 제거

            // 시작 위치 (x, y), N은 세로, M이 가로임
            // 좌표계가 아닌 행렬 좌표로 연산
            // (0, 0) (0, 1) (0, 2)
            // (1, 0) (1, 1) (1, 2)
            // (2, 0) (2, 1) (2, 2)
            for (int x = 0; x <= N - rows; x++) {
                if (isAttach) break;
                for (int y = 0; y <= M - cols; y++) {
                    if (canPlace(x, y, sticker)) {
                        place(x, y, sticker);
                        isAttach = true;
                        break;
                    }
                }
            }

            if (isAttach) return; // 붙였으면 가능하기 때문에 더 돌릴 필요 없이 종료

            // 못 붙였으면 회전하고 다시 처리 (최대 4번 반복함)
            sticker = rotate(sticker);
        }

        // 못 붙이면 폐기
    }

    public static boolean canPlace(int x, int y, int[][] sticker) {
        int rows = sticker.length;
        int cols = sticker[0].length;

        // 그래프 좌표 내부 여부 체크
        if (!(0 <= x && x < N && 0 <= y && y < M)) return false;
        if (x + rows > N || y + cols > M) return false;

        // 겹침 체크 (스티커가 1인 부분은 그래프가 0이어야 함)
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (sticker[i][j] == 1 && graph[x + i][y + j] == 1) {
                    return false;
                }
            }
        }

        return true;
    }

    public static void place(int x, int y, int[][] sticker) {
        int rows = sticker.length;
        int cols = sticker[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (sticker[i][j] == 1) {
                    graph[x + i][y + j] = 1;
                }
            }
        }
    }

    // (0, 0) (0, 1) (0, 2)
    // (1, 0) (1, 1) (1, 2)
    // (2, 0) (2, 1) (2, 2)

    // 90도 회전
    // (2, 0) (1, 0) (0, 0)
    // (2, 1) (1, 1) (0, 1)
    // (2, 2) (1, 2) (0, 2)

    // (a, b) -> (c, d)
    // a: 0 b: 2 -> c: 2 d: 2
    // a: 0 b: 0 -> c: 0 d: 2
    // a: 1 b: 2 -> c: 2 d: 1

    public static int[][] rotate(int[][] sticker) {
        int rows = sticker.length;
        int cols = sticker[0].length;
        int[][] rotatedSticker = new int[cols][rows]; // 회전하므로 행렬 값 변경

        // 회전
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rotatedSticker[j][rows - 1 - i] = sticker[i][j];
            }
        }

        return rotatedSticker;
    }

}   
