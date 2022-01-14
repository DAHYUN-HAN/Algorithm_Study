import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String,String> map = new HashMap<>();//new에서 타입 파라미터 생략가능
        
        for(int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], phone_book[i]);
        }
        
        for(int i = 0; i < phone_book.length; i++) {
            String temp = "";
            for(int j = 0; j < phone_book[i].length(); j++) {
                temp += phone_book[i].charAt(j);
                if(map.get(temp) != null && !map.get(temp).equals(phone_book[i])) {
                    return false;
                }
            }
        }
        
        return answer;
    }
}
