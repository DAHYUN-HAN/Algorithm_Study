import java.util.Arrays;

class marathon_solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        for (int i = 0; i < completion.length; i++) {
            if(!participant[i].equals(completion[i])) {
                answer = participant[i];
                break;
            }
        }
        if(answer == "") {
            answer = participant[participant.length-1];
        }
        return answer;
    }
}

import java.util.HashMap;

class Solution2 {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < participant.length; i++) {
            if(map.get(participant[i]) == null) {
                map.put(participant[i], 1);
            }
            else {
                map.put(participant[i], map.get(participant[i]) + 1);
            }
        }
        
        for(int i = 0; i < completion.length; i++) {
            map.put(completion[i], map.get(completion[i]) - 1);
        }
        
        for(String key : map.keySet()){
            if(map.get(key) != 0) {
                return key;
            }
        }
        
        return "";
    }
}
