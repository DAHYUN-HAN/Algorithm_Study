import java.util.*;
import java.io.*;

class descending {
    public long solution(long n) {
        long answer = 0;
        String stringn = Long.toString(n);
        int length = stringn.length();
        String[] arr = stringn.split("");
        
        Arrays.sort(arr, Collections.reverseOrder());
        String temp_answer = String.join("", arr);
        answer = Long.parseLong(temp_answer);
        return answer;
    }
}
