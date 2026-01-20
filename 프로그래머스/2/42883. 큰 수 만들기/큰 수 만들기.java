import java.util.*;

class Solution {
    public String solution(String number, int k) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        
        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            
            while (!stack.isEmpty() && k > 0 && stack.peekLast() < c) {
                stack.pollLast();
                k--;
            }
            
            stack.offer(c);
        }
        
        // k가 남았다면 추가적으로 뒤에 부분 제거
        while (k > 0) {
            stack.pollLast();
            k--;
        }
        
        StringBuilder sb = new StringBuilder();
        for (char c: stack) {
            sb.append(c);
        }
        
        return sb.toString();
    }
}