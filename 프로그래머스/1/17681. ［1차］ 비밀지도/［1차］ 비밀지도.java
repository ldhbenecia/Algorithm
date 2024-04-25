class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++) {
            String binary1 = Integer.toBinaryString(arr1[i]);
            String binary2 = Integer.toBinaryString(arr2[i]);
            binary1 = String.format("%" + n + "s", binary1).replace(" ", "0");
            binary2 = String.format("%" + n + "s", binary2).replace(" ", "0");
            
            String row = "";
            for (int j = 0; j < n; j++) {
                if (binary1.charAt(j) == '0' && binary2.charAt(j) == '0') {
                    row += " ";
                } else {
                    row += "#";
                }
            }
            
            answer[i] = row;
        }
        
        return answer;
    }
}