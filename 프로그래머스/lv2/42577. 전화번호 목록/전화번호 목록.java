import java.util.*;

// class Solution {
//     public boolean solution(String[] phone_book) {
//         boolean answer = true;

//         Map<Integer, String> map = new HashMap<>();

//         for (int i = 0; i < phone_book.length; i++) {
//             map.put(i ,phone_book[i]);
//         }

//         for (int i = 0; i < phone_book.length; i++) {
//             for (int j = 0; j < phone_book[i].length(); j++) {
//                 if (map.containsValue(phone_book[i].substring(0, j))) {
//                     answer = false;
//                 }
//             }
//         }

//         return answer;

//     }
// }

class Solution {
    public boolean solution(String[] phoneBook) {
        Arrays.sort(phoneBook);
        boolean result = true;
        for (int i=0; i<phoneBook.length-1; i++) {
            if (phoneBook[i+1].startsWith(phoneBook[i])) {
                result = false;
                break;
            }
        }
        return result;
    }
}