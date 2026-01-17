import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new ArrayDeque<>();
        int time = 0;
        int currentWeight = 0;
        int idx = 0;

        // 다리를 빈 칸(0)으로 미리 채움
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }

        while (idx < truck_weights.length) {
            time++;

            // 1. 한 칸 이동
            currentWeight -= bridge.poll();

            // 2. 트럭 진입 가능 여부
            if (currentWeight + truck_weights[idx] <= weight) {
                bridge.offer(truck_weights[idx]);
                currentWeight += truck_weights[idx];
                idx++;
            } else {
                bridge.offer(0);
            }
        }

        // 마지막 트럭이 다리를 건너는 시간
        return time + bridge_length;
    }
}
