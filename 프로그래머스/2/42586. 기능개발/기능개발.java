import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int maxPercent = 100;
        
        List<Integer> time = new ArrayList<>();
        for (int i = 0; i < speeds.length; i++) {
            int remaining = maxPercent - progresses[i];
            int days = (int) Math.ceil((double) remaining / speeds[i]);
            time.add(days);
        }
        
        int count = 1;
        int currentMax = time.get(0);
        for (int i = 1; i < time.size(); i++) {
            if (time.get(i) <= currentMax) {
                count ++;
            } else {
                answer.add(count);
                count = 1;
                currentMax = time.get(i);
            }
        }
        
        answer.add(count);
        return answer;
    }
}
