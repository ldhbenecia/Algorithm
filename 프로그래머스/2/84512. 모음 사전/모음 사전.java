class Solution {
    
    private char[] alphabetList = new char[]{'A', 'E', 'I', 'O', 'U'};
    private int idx = 0;
    private int result = 0;
    
    public void dfs(int cnt, String alphabet, String word) {
        
        if (alphabet.equals(word)) {
            result = idx;
            return;
        }
        
        if (cnt == 5) {
            return;
        }
        
        for (int i = 0; i < 5; i++) {
            idx++;
            dfs(cnt + 1, alphabet + alphabetList[i], word);
        }
    }
    
    public int solution(String word) {
        dfs(0, "", word);
        return result;
    }
}