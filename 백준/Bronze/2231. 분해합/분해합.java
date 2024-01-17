import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        final int N = Integer.parseInt(br.readLine());
        System.out.println(solution(N));


        /*
         * 1.스트링
         * 스트링 길이는 가능
         * 스트링 toCharArray 가능
         * */

        /*
         * 2. 스트링 배열
         * 스트링 길이 가능
         * 스트링 배열 접근 가능
         * */

        /*
         * 3. 스트림
         *  스트링 배열로 만들어서 형 변환 및 합계까지 구한다.
         * */

    }

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
