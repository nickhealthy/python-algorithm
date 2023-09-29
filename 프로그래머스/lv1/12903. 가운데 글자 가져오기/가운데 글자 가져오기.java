class Solution {
    public String solution(String s) {
        String answer = "";
        final int sLengths = s.length();
        if (sLengths % 2 == 0) {
            answer = s.substring((sLengths - 1) / 2, sLengths / 2 + 1);
        } else {
            answer = s.substring(sLengths / 2, sLengths / 2 + 1);
        }
        return answer;
    }   
}