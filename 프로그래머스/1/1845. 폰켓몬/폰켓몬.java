import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        
        // 종류 번호, 마릿수 저장
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        int possible = nums.length / 2;
        // possible 개수만큼 가져가도 됨
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (possible == 0) break;
            
            if (entry.getValue() > 0) {
                answer++;
                possible--;
            }
        }
        
        
        
        return answer;
    }
}