import java.util.*;

class Solution {
    
    private void combine(char[] menus, String current, int index, int r, Map<String, Integer> counting) {
        if (current.length() == r) {
            counting.put(current, counting.getOrDefault(current, 0) + 1);
            return;
        }

        for (int i = index; i < menus.length; i++) {
            combine(menus, current + menus[i], i + 1, r, counting);
        }
    }
    
    public List<String> solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        Map<String, Integer> counting = new HashMap<>();
        
        for (String order : orders) {
            char[] menus = order.toCharArray();
            Arrays.sort(menus);
            
            int len = menus.length;
            for (int r : course) {
                if (r > len) continue; // course의 크기가 메뉴의 수보다 크면 건너뜀 (2개 이상 거르기 위함)
                combine(menus, "", 0, r, counting); // 조합을 생성하고 카운트
            }
        }
        
        for (int r : course) {
            int maxCount = 0;

            // 현재 코스의 최대 카운트를 찾기
            for (Map.Entry<String, Integer> entry : counting.entrySet()) {
                if (entry.getKey().length() == r) { // 현재 코스 크기와 일치하는 조합
    
                    // 추출해낸 조합에서 길이 순서에서 maxCount(가장 많이 주문 된 것들 추출)
                    maxCount = Math.max(maxCount, entry.getValue());
                }
            }

            // 최대 카운트에 해당하는 조합을 결과에 추가
            for (Map.Entry<String, Integer> entry : counting.entrySet()) {
                if (entry.getValue() == maxCount && maxCount > 1 && entry.getKey().length() == r) {
                    answer.add(entry.getKey());
                }
            }
        }
        
        Collections.sort(answer);
        return answer;
    }
}