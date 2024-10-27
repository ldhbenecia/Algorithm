import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, List<String>> clothMap = new HashMap<>();

        for (int i = 0; i < clothes.length; i++) {
            String name = clothes[i][0];
            String type = clothes[i][1];
            
            if (!clothMap.containsKey(type)) {
                clothMap.put(type, new ArrayList<>());
            }
            clothMap.get(type).add(name);
        }
        
        
        int answer = 1; // default
        for (List<String> c : clothMap.values()) {
            answer *= (c.size() + 1);
        }
        
        return answer - 1;
    }
}