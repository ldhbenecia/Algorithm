import java.util.*;

class Solution {
    public List<Integer> solution(int[] answers) {
        int[] answer = {};
        
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int firstCorrect = 0;
        int secondCorrect = 0;
        int thirdCorrect = 0;
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == first[i % first.length]) firstCorrect ++;
            if (answers[i] == second[i % second.length]) secondCorrect ++;
            if (answers[i] == third[i % third.length]) thirdCorrect ++;
        }
        
        int maxScore = Math.max(firstCorrect, Math.max(secondCorrect, thirdCorrect));
        
        List<Integer> topScores = new ArrayList<>();
        if (firstCorrect == maxScore) topScores.add(1);
        if (secondCorrect == maxScore) topScores.add(2);
        if (thirdCorrect == maxScore) topScores.add(3);
        
        return topScores;
    }
}