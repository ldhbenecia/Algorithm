import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        
        // 동명이인이 있을 수 있기 때문에 이름과 몇 명인지 연산
        for (String name : participant) {
            map.put(name, map.getOrDefault(name, 0) + 1);
        }
        
        // 완주한 사람 빼기
        for (String name : completion) {
            map.put(name, map.get(name) - 1);
        }
        
        // map에 0이 아닌 사람 추출하면 답
        // Entry를 사용할 때는 getKey(), getValue()만 사용
        // Map에서 꺼낼 때는 ketSet(), values() 사용
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() != 0) {
                return entry.getKey();
            }
        }
        
        return "";
    }
}