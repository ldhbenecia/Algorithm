import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        
        Arrays.sort(targets, ((a, b) -> Integer.compare(a[0], b[0])));
        
        int preStart = targets[0][0];
        int preEnd = targets[0][1];
        
        for (int[] target : targets) {
            int s = target[0];
            int e = target[1];
            
            if (preStart <= s && s < preEnd) {
                preStart = Math.max(preStart, s);
                preEnd = Math.min(preEnd, e);
            } else {
                preStart = s;
                preEnd = e;
                answer += 1;
            }
        }
        
        return answer;
    }
}