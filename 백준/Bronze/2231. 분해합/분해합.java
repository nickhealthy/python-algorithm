import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.IntStream;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        final int N = Integer.parseInt(br.readLine());
        int start = N - String.valueOf(N).length() * 9;

        /* 스트림 두 번째 풀이 */
        int answer = IntStream.range(start, N)
                .filter(value ->
                        String.valueOf(value).chars().map(Character::getNumericValue).sum() + value
                                == N)
                .findFirst()
                .orElse(0);

        /* 스트림 첫 번째 풀이 */
//        int answer = 0;
//        for (int i = start; i < N; i++) {
//
//            int sum = String.valueOf(i)
//                    .chars()
//                    .map(Character::getNumericValue)
//                    .sum();
//
//            if (sum + i == N) {
//                answer = i;
//                break;
//            }
//        }

        /* 정통적인 방식 첫 번째 풀이 */
//        answer = solution(N);

        System.out.println(answer);

    }

    /* 정통적인 방식 첫 번째 풀이 */
    private static int solution(int N) {

        for (int i = 1; i < N; i++) {
            int answer = 0;

            char[] charArray = String.valueOf(i).toCharArray();
            for (char c : charArray) {
                answer += Character.getNumericValue(c);
            }

            if (answer + i == N) {
                return i;
            }
        }

        return 0;
    }
}
