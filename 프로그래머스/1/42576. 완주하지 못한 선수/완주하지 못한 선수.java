import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> participantCount = new HashMap<>();
        
        for (String p : participant) {
            participantCount.put(p, participantCount.getOrDefault(p, 0) + 1);
        }
        
        for (String c : completion) {
            participantCount.put(c, participantCount.get(c) - 1);
        }
        
        for (String p : participantCount.keySet()) {
            if (participantCount.get(p) > 0) {
                return p;
            }
        }

        return "";
    }
}