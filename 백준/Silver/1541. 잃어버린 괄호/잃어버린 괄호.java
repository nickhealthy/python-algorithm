import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String params = br.readLine();

        int answer = calculate(params);
        System.out.println(answer);
    }

    private static int calculate(String params) {
        String[] arr = params.split("\\-");

        // 첫 번째로 나오는 마이너스를 기준으로 왼쪽은 더해주고, 오른쪽은 모두 빼주면 됨
        int answer = sum(arr[0]);

        // 첫 번째는 무조건 양수
        for (int i = 1; i < arr.length; i++) {
            answer -= sum(arr[i]);
        }

        return answer;
    }

    private static int sum(String s) {
        String[] sumArr = s.split("\\+");
        int result = 0;
        for (String num : sumArr) {
            result += Integer.parseInt(num);
        }
        return result;
    }
}
