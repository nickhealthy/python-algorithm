// import java.util.*;

// class Solution {
//     public String solution(String[] participant, String[] completion) {
//         String answer = "";

//         Map<String, Integer> map = new HashMap<>();
//         for (int i = 0; i < completion.length; i++) {
//             map.put(completion[i], 1);
//         }

//         for (int i = 0; i < completion.length; i++) {
//             if (!(map.containsKey(participant[i]))) {
//                 answer = participant[i];
//             }
//         }
//         return answer;
//     }
// }

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        Map<String, Integer> map = new HashMap<>();
        for(String name: participant) map.put(name, map.getOrDefault(name, 0) + 1);

        for(String name: completion) {
            map.put(name, map.get(name) - 1);
        }

        for(String key: map.keySet()) {
            if (map.get(key) != 0) {
                answer = key;
            }
        }

        return answer;
 }
}
