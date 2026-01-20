import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        Arrays.sort(rocks);
        
        int left = 1;
        int right = distance;

        while (left <= right) {
            int mid = (left + right) / 2;
            
            int prev = 0; // 이전 바위 위치 (시작점 0으로 초기화)
            int removeCount = 0; // 제거한 바위 개수
            
            // 출발점부터 바위, 바위 <-> 바위 구간 비교
            for (int rock : rocks) {
                if (rock - prev < mid) {
                    // 최소 거리 불만족
                    removeCount++;
                } else {
                    // 유지 가능
                    prev = rock;
                }
            }
            
            // 출발점이랑 비교했으니까 도착점까지의 거리도 비교해야함
            if (distance - prev < mid) {
                removeCount++;
            }
            
            // 2 11 14 17 21 //// 2, 11제거, prev 14 17제거, 21 제거
            
            // 거리 최솟값이 distance가 25여서 13이라고 두자.
            // 시작점 0으로부터 2는 거리가 2니까 제거
            // 11 제거
            // 14 세이브
            // 14와 17은 3이니까 제거
            // 14와 21은 7이니까 제거
            
            System.out.println(removeCount); // 4개 잘 나옴
            
            // n보다 크니까 right를 줄여야함
            if (removeCount > n) {
                right = mid - 1;
            } else {
                answer = mid;
                left = mid + 1;
            }
        }
        
        return answer;
    }
}