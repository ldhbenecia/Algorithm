class Solution {
    public int solution(int n) {
        String ternary = Integer.toString(n, 3); // 3진수 변환
        String reversed = new StringBuilder(ternary).reverse().toString(); // 3진수 변환 문자열 뒤집기
        int answer = Integer.parseInt(reversed, 3); // 3진수 문자열 10진수로 변환
        return answer;
    }
}