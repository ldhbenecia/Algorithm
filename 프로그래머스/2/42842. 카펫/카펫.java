class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int total = brown + yellow;
        
        for (int height = 3; height <= total; height++) {
            if (total % height == 0) {
                int width = total / height;
                
                if (width >= height) {
                    if ((width - 2) * (height - 2) == yellow) {
                        answer[0] = width;
                        answer[1] = height;
                    }
                }
            }
        }
        
        return answer;
    }
}