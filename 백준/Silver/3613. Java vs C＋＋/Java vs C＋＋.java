import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String word = br.readLine();
        char underBar = '_';

        if (word.isEmpty() || word.startsWith("_") || word.endsWith("_")) {
            bw.write("Error!");
            bw.flush();
            return;
        }

        // Java는 첫 단어는 소문자, 다음 단어부터는 대문자로 사용, 모든 단어는 붙여 씀
        // C++의 경우 대문자를 사용하지 않고 구분하기 위해 _ 사용
        boolean hasUnder = false;
        boolean hasUpper = false;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (c == underBar) hasUnder = true;
            if (Character.isUpperCase(c)) hasUpper = true;
        }

        // 둘다 true면 불가능
        if (hasUnder && hasUpper) {
            bw.write("Error!");
            bw.flush();
            return;
        }

        StringBuilder sb = new StringBuilder();

        // Java -> C++
        if (!hasUnder) {
            // 첫 글자가 대문자면 에러
            if (Character.isUpperCase(word.charAt(0))) {
                bw.write("Error!");
                bw.flush();
                return;
            }

            // 순회하면서 대문자가 나오면 언더바 삽입 후 소문자로 전환 후 삽입
            for (char c : word.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    sb.append(underBar);
                    sb.append(Character.toLowerCase(c));
                } else {
                    sb.append(c);
                }
            }
        } else {
            // C++ -> Java
            // 순회하면서 언더바가 나오면 제거 후 대문자 전환 후 삽입

            if (Character.isUpperCase(word.charAt(0))) {
                bw.write("Error!");
                bw.flush();
                return;
            }

            boolean isUnder = false;
            for (char c : word.toCharArray()) {
                if (c == underBar) {
                    // __ 2개 처리
                    if (isUnder) {
                        bw.write("Error!");
                        bw.flush();
                        return;
                    }
                    isUnder = true; // 언더바가 나오면 sb.append 안함
                } else {
                    // 언더바가 나온 이후 값은 대문자로 바꾸어서 삽입
                    if (isUnder) {
                        sb.append(Character.toUpperCase(c));
                        isUnder = false;
                    } else {
                        sb.append(c);
                    }
                }
            }
        }

        bw.write(sb.toString());
        bw.flush();
    }
}   
