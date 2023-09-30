import java.util.*;

class Solution {
    public int solution(int[] nums) {
         int answer = 0;
        int count = nums.length / 2;
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(map.get(nums[i]), 0) + 1);
        }

//        System.out.println(map.size());
        // nums / 2 만큼만 가져갈 수 있다.
        // 누구꺼를 가져갔는지 체크해야하는데..
        // 그냥 루프만 돌면 되지 않을까?
        if (map.size() >= count) {
            answer = count;
        } else if (map.size() < count) {
            answer = map.size();
        }

        return answer;
    }
}