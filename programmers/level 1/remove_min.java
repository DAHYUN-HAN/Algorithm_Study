class remove_min {
    public int[] solution(int[] arr) {
        if(arr.length == 1) {
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[arr.length-1];
        
        int min = Integer.MAX_VALUE;
        int index = -1;
        for (int i = 0; i < arr.length; i++) {
            if(min > arr[i]) {
                index = i;
                min = arr[i];
            }
        }
        
        for(int i = 0; i < arr.length-1; i++) {
            if(i < index) {
                answer[i] = arr[i];
            }
            else {
                answer[i] = arr[i+1];
            }
        }
        
        return answer;
    }
}
