import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        for (int i = 0; i < reserve.length; i++) {
            for (int j = 0; j < lost.length; j++) {
                if (reserve[i] == lost[j]) {
                    answer++; // 이 학생은 여분이 있으므로 참여 가능
                    lost[j] = -1; // 불가 표시
                    reserve[i] = -1; // 불가 표시
                    break;
                }
            }
        }
        
        // 자기 번호로부터 +1, -1인 것만 가능
        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if (lost[i] - 1 == reserve[j] || lost[i] + 1 == reserve[j]) {
                    answer++;
                    reserve[j] = -1; // 빌려줌 표시
                    break;
                }
            }
        }
        
        return answer;
    }
}