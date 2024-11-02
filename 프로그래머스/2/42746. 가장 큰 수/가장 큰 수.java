import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] answer = new String[numbers.length];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(answer, (v1, v2) -> (v2 + v1).compareTo(v1 + v2));
        
        if (answer[0].equals("0")) {
            return "0";
        }
        
        return String.join("", answer);
    }
}