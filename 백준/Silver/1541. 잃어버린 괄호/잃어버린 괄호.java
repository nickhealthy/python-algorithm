import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String params = br.readLine();

        String[] arr = params.split("\\-");
        String[] sumArr = arr[0].split("\\+");
        for (int i = 0; i < sumArr.length; i++) {
            answer += Integer.valueOf(sumArr[i]);
        }

        // 첫 번째로 나오는 마이너스를 기준으로 왼쪽은 더해주고, 오른쪽은 모두 빼주면 됨
        // 첫 번째는 무조건 양수
        for (int i = 1; i < arr.length; i++) {
            String[] localArr = arr[i].split("\\+");
            for (int j = 0; j < localArr.length; j++) {
                answer -= Integer.valueOf(localArr[j]);
            }
        }

        System.out.println(answer);


    }

}
