import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int MAX_VALUE = Integer.MIN_VALUE;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        int N = Integer.valueOf(tokenizer.nextToken());
        int M = Integer.valueOf(tokenizer.nextToken());

        /* 스트림을 이용한 배열 입력 방식1 */
        // filter()를 이용해서 공백을 제거해주어야 한다.
//        int[] array = br.readLine().chars().filter(c -> c != ' ').map(Character::getNumericValue)
//                .toArray();

        /* 스트림을 이용한 배열 입력 방식2 */
        int[] array = Arrays.stream(br.readLine().split("\\s+"))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int i = 0; i < array.length - 2; i++) {

            for (int j = i + 1; j < array.length - 1; j++) {

                for (int k = j + 1; k < array.length; k++) {

                    int deck_sum = sumThreeInteger(array[i] + array[j] + array[k]);

                    if (deck_sum <= M) {
                        MAX_VALUE = Math.max(MAX_VALUE, deck_sum);
                    }

                }
            }

        } // for 끝

        System.out.println(MAX_VALUE);
    }

    private static int sumThreeInteger(int... numbers) {

        return Arrays.stream(numbers).sum();

    }
}
