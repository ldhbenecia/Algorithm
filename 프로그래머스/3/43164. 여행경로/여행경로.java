import java.util.*;

class Solution {
    
    public boolean dfs(String start, String[][] tickets, boolean[] visited, ArrayList<String> path) {
        // base
        if (path.size() == tickets.length + 1) {
            return true;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0].equals(start)) {
                visited[i] = true;
                path.add(tickets[i][1]);
                
                if (dfs(tickets[i][1], tickets, visited, path)) {
                    return true;
                }
                
                // 백트래킹
                visited[i] = false;
                path.remove(path.size() - 1);
            }
        }
        
        return false;
    }
    
    public String[] solution(String[][] tickets) {
        // 람다식을 써서 도착지를 알파벳 순으로 정렬 후 탐색을 통해서 경로 추출
        Arrays.sort(tickets, (a, b) -> a[1].compareTo(b[1]));
        System.out.println(Arrays.deepToString(tickets));
        
        boolean[] visited = new boolean[tickets.length];
        ArrayList<String> path = new ArrayList<>();
        
        path.add("ICN");
        dfs("ICN", tickets, visited, path);
        
        // ArrayList를 변환하기 위해서 toArray(new String[0])을 사용함
        // toArray는 Object[]를 반환하는데 String[]으로 타입 지정을 해주기 위해서 new String[0]을 사용함
        return path.toArray(new String[0]);
    }
}