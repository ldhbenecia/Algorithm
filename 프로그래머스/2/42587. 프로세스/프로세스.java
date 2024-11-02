import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<Integer> queue = new LinkedList();
        List<Integer> alphabetIdx = new ArrayList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            queue.add(priorities[i]);
            alphabetIdx.add(i);
        }
        
        while (!queue.isEmpty()) {
            int currentPriority = queue.poll();
            int currentIdx = alphabetIdx.remove(0);
            
            boolean hasHigher = false;
            for (int priority : queue) {
                if (priority > currentPriority) {
                    hasHigher = true;
                    break;
                }
            }
            
            // 더 높은 우선순위를 가진 값이 있다면
            if (hasHigher) {
                queue.add(currentPriority);
                alphabetIdx.add(currentIdx);
            } else {
                answer++;
                
                if (currentIdx == location) {
                    return answer;
                }
            }
        }
        
        return answer;
    }
}