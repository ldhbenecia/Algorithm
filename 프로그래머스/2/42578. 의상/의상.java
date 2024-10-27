import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothMap = new HashMap<>();

        for (int i = 0; i < clothes.length; i++) {
            String type = clothes[i][1];
            clothMap.put(type, clothMap.getOrDefault(type, 0) + 1);
        }
        
        int answer = 1; // default
        for (String key : clothMap.keySet()) {
            answer *= (clothMap.get(key) + 1);
        }
        
        return answer - 1;
    }
}