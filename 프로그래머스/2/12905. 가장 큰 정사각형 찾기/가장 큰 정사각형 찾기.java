class Solution
{
    public int solution(int [][]board)
    {
        int n = board.length;
        int m = board[0].length;
        
        int[][] dp = new int[n][m];
        int maxSide = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 1) {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1;
                    } else {
                        // 현재 위치로부터 왼쪽, 위쪽, 왼쪽윗대각을 비교한다. 단 여기서 최솟값을 찾는다.
                        // 최솟값을 찾는 이유: 0인 경우 0 1
                        //                        1 1  인 경우라면 정사각형이 되지 않기 때문에 정사각형 크기는 1이다.
                        //                        최솟값이 0이니까 0 + 1 해서 정사각형 크기는 1 저장
                        // 1 1
                        // 1 1 이라면 정사각형 크기는 2가 되니까 dp 테이블에서 오른쪽아래 현재 위치값을 += 1해서 2로 바꿔준다.
                        // 1 1 1
                        // 1 2 2
                        // 1 2 3 이렇게 최솟값을 찾아서 + 1을 하다보면 왼쪽, 위쪽, 윗대각이 모두 2가 되면 3이 될 것이다.
                        // 이는 board 판이 1 1 1
                        //               1 1 1
                        //               1 1 1 이 되었고 이러면 정사각형 길이는 3이 되게 된다.
                        dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                    }
                    maxSide = Math.max(maxSide, dp[i][j]);        
                } else {
                    dp[i][j] = 0;
                }
            }
        }
        
        return maxSide * maxSide;
    }
}