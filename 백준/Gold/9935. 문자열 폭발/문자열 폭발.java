import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String originalStrings = br.readLine();
        char[] bombString = br.readLine().toCharArray();

        final int BOMB_STRING_LENGTH = bombString.length;

        Stack<Character> stack = new Stack<>();
        for (char c : originalStrings.toCharArray()) {

            stack.push(c);

            boolean flag = true;
            if (stack.size() >= BOMB_STRING_LENGTH) {
                for (int i = 0; i < BOMB_STRING_LENGTH; i++) {
                    if (stack.get(stack.size() - 1 - i) != bombString[BOMB_STRING_LENGTH - 1 - i]) {
                        flag = false;
                        break;
                    }
                } // for 끝
            }

            // stack 안에 폭탄 문자열이 포함되어 있다면
            if (flag && stack.size() >= BOMB_STRING_LENGTH) {
                for (int i = 0; i < BOMB_STRING_LENGTH; i++) {
                    stack.pop();
                }
            }
        } // for 끝

        if (stack.isEmpty()) {
            System.out.println("FRULA");
        } else {
            StringBuilder sb = new StringBuilder();
            for (char c : stack) {
                sb.append(c);
            }
            System.out.println(sb);
        }

    }
}
