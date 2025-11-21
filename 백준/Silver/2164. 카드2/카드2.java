import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        int N = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> cards = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            cards.offer(i + 1);
        }

        while (cards.size() > 1) {
            cards.pollFirst();
            cards.offerLast(cards.pollFirst());
        }

        bw.write(cards.peek() + "\n");
        bw.flush();
    }
}   
