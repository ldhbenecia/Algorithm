import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        // N시간
        // 야근 피로도: 시작한 시점 + 남은일의작업량^2
        // 1시간 동안 1만큼 작업 처리 가능
        
        // 퇴근하고 4시간이 남고 각 일에대한 작업량이 [4,3,3]이 있음
        // 야근 피로도를 최소화한 값
        // 4 3 3 -> 3 3 3 -> 3 2 3 -> 3 2 2 -> 2 2 2
        // 1시간당 1번이니까 이렇게 하나씩 줄임
        
        // 최소화를 하기 위해서는 큰 값부터 없애야함
        // 동시에 효율성을 지키기 위해서 특정 자료구조를 사용해야함
        // 우선순위큐 사용 -> 최대힙 사용
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int w : works) {
            maxHeap.offer(w);
        }

        for (int i = 0; i < n; i++) {
            if (maxHeap.isEmpty()) {
                break;
            }

            int top = maxHeap.poll();
            if (top == 0) {
                break;
            }
            maxHeap.offer(top - 1);
        }
        
        for (long w : maxHeap) {
            answer += w * w;
        }
        
        
        return answer;
    }
}