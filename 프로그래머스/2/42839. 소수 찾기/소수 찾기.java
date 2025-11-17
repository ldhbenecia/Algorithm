import java.util.*;

class Solution {
    boolean[] visited;
    Set<Integer> lst = new HashSet<>();
    
    private boolean isPrime(int n) {
        if (n < 2) return false;
        
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        
        return true;
    }
    
    private void dfs(String numbers, String current, int length) {
        // base
        if (current.length() == length) {
            int num = Integer.parseInt(current);
            lst.add(num);
            return;
        }
            
        for (int i = 0; i < numbers.length(); i++) {
            
            if (!visited[i]) {
                visited[i] = true;
                dfs(numbers, current + numbers.charAt(i), length);
                visited[i] = false;
            }
        }
    }
    
    public int solution(String numbers) {
        int answer = 0;
        visited = new boolean[numbers.length()];
        
        for (int i = 0; i < numbers.length(); i++) {
            dfs(numbers, "", i+1);
        }
        
        for (int x : lst) {
            if (isPrime(x)) answer++;
        }
        
        return answer;
    }
}