class Solution {
    private int cnt = 0;
    
    private void dfs(int[] numbers, int target, int current, int idx) {
        if (numbers.length == idx) {
            if (current == target) {
                cnt ++;
            }
            return;
        }
        
        dfs(numbers, target, current + numbers[idx], idx + 1);
        dfs(numbers, target, current - numbers[idx], idx + 1);
    }
    
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return cnt;
    }
}