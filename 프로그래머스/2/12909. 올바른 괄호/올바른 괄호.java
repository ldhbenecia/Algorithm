import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        List<Character> basket = new ArrayList<>();
        
        // 여는 괄호 개수 (닫은 괄호 개수와 비교하기 위함)
        int openCount = 0;
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            basket.add(currentChar);   
            
            if (currentChar == '(') {
                openCount++;
            } else {
                openCount--;
            }
            
            if (openCount < 0) {
                return false;
            }
        }
        
        if (openCount != 0) {
            return false;
        }                    
        
        return answer;
    }
}