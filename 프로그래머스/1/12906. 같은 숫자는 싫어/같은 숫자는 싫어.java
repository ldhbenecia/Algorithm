import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> stack = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (stack.isEmpty() || stack.get(stack.size() - 1) != arr[i]) {
                stack.add(arr[i]);
            }
        }
    
        int[] answer = new int[stack.size()];
        for (int i = 0; i < stack.size(); i++) {
            answer[i] = stack.get(i);
        }

        return answer;
    }
}