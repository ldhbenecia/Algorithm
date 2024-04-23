import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        List<int[]> answerList = new ArrayList<>();
        int left = 0;
        int right = 0;
        int sequence_sum = sequence[0];
        
        if (sequence_sum == k) {
            return new int[]{0, 0};
        }
        
        while (true) {
            if (sequence_sum <= k) {
                right += 1;
                if (right == sequence.length) break;
                sequence_sum += sequence[right];
            } else {
                left += 1;
                sequence_sum -= sequence[left - 1];
            }
            
            if (sequence_sum == k) {
                answerList.add(new int[]{left, right});
            }
        }
        
        // for (int[] arr : answerList) {
        //     System.out.println(Arrays.toString(arr));
        // }
        
        int minDiff = Integer.MAX_VALUE;
        int[] result = null;
        for (int[] answer : answerList) {
            int diff = answer[1] - answer[0];
            if (diff < minDiff) {
                minDiff = diff;
                result = answer;
            }
        }
        
        return result;
    }
}