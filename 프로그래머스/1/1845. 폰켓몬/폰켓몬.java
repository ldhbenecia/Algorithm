import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int target = nums.length / 2;
        
        Set<Integer> uniqueNumbers = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            uniqueNumbers.add(nums[i]);
        }
 
        if (uniqueNumbers.size() >= target) {
            answer = target;
        } else {
            answer = uniqueNumbers.size();
        }
        
        return answer;
    }
}