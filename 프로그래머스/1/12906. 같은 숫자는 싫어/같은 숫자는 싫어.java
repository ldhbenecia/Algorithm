import java.util.*;

public class Solution {
    public List<Integer> solution(int []arr) {
        List<Integer> stack = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (stack.isEmpty() || stack.get(stack.size() - 1) != arr[i]) {
                stack.add(arr[i]);
            }
        }

        return stack;
    }
}