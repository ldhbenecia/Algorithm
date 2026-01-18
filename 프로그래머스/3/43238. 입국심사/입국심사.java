import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        
        // n, times 시간 범위 값으로 보아 O(n)선에서 해결해야함
        
        // 6, [7, 10] = 28
        // 6명을 심사하려면 28초가 걸림
        long left = 0;
        long right = 0;
        
        for (int t : times) {
            right = Math.max(right, t);
        }
        right *= n;
        
        answer = right; // 최악의 경우의 수 제일 오래 걸리는 시간으로 인원 수만큼 심사한 시간 초기화
        
        while (left <= right) {
            long mid = (left + right) / 2; // 33
            
            // 33분 동안 심사할 수 있는 사람 개수 구하기
            long possible = 0;
            for (int time : times) {
                possible += mid / time; // 33 / 7 = 4, 33 / 10 = 3 -> 7임
                // 7이면 n보다 크기 때문에 더 쪼개야함
                
                if (possible >= n) break;
            }
            
            if (possible >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }
        
        return answer;
    }
}