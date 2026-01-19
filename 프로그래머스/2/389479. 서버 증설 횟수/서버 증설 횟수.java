import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int time = 0;
        
        ArrayList<Integer> onTime = new ArrayList<>();

        for (int player : players) {
            int now = time;
            // 현재 시각이 서버 종료 시간을 지났으면 해당 서버 증설 기록 제거
            onTime.removeIf(end -> now >= end);
            
            int requiredServer = player / m;
            int current = onTime.size();
            
            // 게임 이용자의 수 / 서버 증설 필요 인원 수를 통해서 현재 증설된 서버 개수보다 더 필요할 경우에만 증설
            if (requiredServer > current) {
                int need = requiredServer - current;
                
                // 더 필요한 수 만큼 현재 시간으로부터 +k 값 기록
                for (int i = 0; i < need; i++) {
                    onTime.add(time + k);
                    answer++;
                }
            }
            
            time++;
        }
        
        return answer;
    }
}