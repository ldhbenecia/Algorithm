import java.util.*;

class Solution {
    
    private int answer = 0;;
    
    public int solution(int n, int[][] q, int[] ans) {
        List<Integer> current = new ArrayList<>();
        comb(0, 1, current, n, q, ans);
        return answer;
    }
    
    // depth: 현재까지 뽑은 개수
    // start: 다음에 뽑을 수 있는 시작 숫자 (조합용)
    private void comb(int depth, int start, List<Integer> current, int n, int[][] q, int[] ans) {
        if (depth == 5) {
            if (correct(current, q, ans)) answer++;
            return;
        }
        
        for (int i = start; i <= n; i++) {
            current.add(i);
            comb(depth + 1, i + 1, current, n, q, ans);
            current.remove(current.size() - 1);
        }
    }
    
    private boolean correct(List<Integer> current, int[][] q, int[] ans) {
        for (int i = 0; i < q.length; i++) {
            int count = 0;
            
            for (int num : q[i]) {
                if (current.contains(num)) {
                    count++;
                }
            }
            
            if (count != ans[i]) {
                return false;
            }
        }
        
        return true;
    }
}
