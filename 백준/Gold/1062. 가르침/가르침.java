import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int N, K, answer;
    static boolean[] visited = new boolean[26];
    static String[] words;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.valueOf(input[0]);
        K = Integer.valueOf(input[1]);

        if (K < 5) {
            System.out.println("0");
            return;
        } else if (K == 26) {
            System.out.println(N);
            return;
        }

        words = new String[N];
        for (int i = 0; i < N; i++) {
            String parseString = br.readLine();
            words[i] = parseString.substring(4, parseString.length() - 4);
        }

        // visted base_char 초기화
        for (char c : "acint".toCharArray()) {
            visited[c - 'a'] = true;
        }

        backTracking(0, 0);
        System.out.println(answer);
    }

    private static void backTracking(int alpha, int len) {

        if (len == K - 5) {
            int count = 0;
            for (int i = 0; i < words.length; i++) { // 뽑은 알파벳으로 몇 개의 단어를 읽을 수 있는지 카운트
                boolean read = true;

                for (int j = 0; j < words[i].length(); j++) {
                    if (!visited[words[i].charAt(j) - 'a']) {
                        read = false;
                        break;
                    }
                }

                if (read) {
                    count++;
                }
            }

            answer = Math.max(answer, count);
            return;
        }

        for (int i = alpha; i < 26; i++) {
            if (!visited[i]) {
                visited[i] = true;
                backTracking(i, len + 1);
                visited[i] = false;
            }
        }

    }

}
