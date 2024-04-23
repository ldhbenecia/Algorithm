import java.util.*;

class Word {
    String word;
    int idx;
    
    Word(String word, int idx) {
        this.word = word;
        this.idx = idx;
    }
}

class Solution {
    
    public int bfs(String begin, String target, String[] words) {
        Queue<Word> queue = new LinkedList<>();
        queue.offer(new Word(begin, 0));
        
        while (!queue.isEmpty()) {
            Word currentWord = queue.poll();
            
            if (currentWord.word.equals(target)) {
                return currentWord.idx;
            }
            
            for (String word : words) {
                int cnt = 0;
                for (int j = 0; j < currentWord.word.length(); j++) {
                    if (currentWord.word.charAt(j) != word.charAt(j)) {
                        cnt++;
                    }
                }
                
                if (cnt == 1) {
                    queue.offer(new Word(word, currentWord.idx + 1));
                }
            }
        }
        
        return 0;
    }
    
    public int solution(String begin, String target, String[] words) {
        boolean containsTarget = Arrays.asList(words).contains(target);
        if (!containsTarget) {
            return 0;
        }
        
        return bfs(begin, target, words);
    }
}