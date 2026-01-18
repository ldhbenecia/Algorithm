import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        if (s < n) {
            return new int[]{-1};
        }

        int[] answer = new int[n];
        
        // 원소의 개수: n
        // n개의 숫자의 합이 s를 만족하는 집합 찾기
        // 해당 집합들 중 원소의 곱이 가장 큰 집합 찾기
        
        // 뽑은 집합은 배열 형식으로 반환하되 오름차순으로 정렬 후 반환할 것
        // 최고의 집합이 존재하지 않으면 [-1] 반환
        
        // 반복문은 s까지 잡고 돌리기 (s보다 큰 합이 나올 수 없음)        
        // 문제점 n의 개수만큼 반복문을 돌려야하는가? 시간 복잡도 초과 위험 가능
        // 수식으로 해결
        int base = s / n; // 9 / 2 = 4
        int remain = s % n; // 9 % 2 = 1
        
        for (int i = 0; i < n; i++) {
            answer[i] = base;
        }
        
        for (int i = 0; i < remain; i++) {
            answer[i]++;
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}