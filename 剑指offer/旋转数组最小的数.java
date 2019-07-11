import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        int l = array.length;
        if(l == 0)
            return 0;
        int s = 0;
        int e = l - 1;
        while(s < e){
            int m = (s + e) / 2;
            if(array[m] > array[e])
                s = m + 1;
            else if(array[m] == array[e])
                e = e - 1;
            else
                e = m;
        }
        return array[e];
    }
    
    public int burcemin(int [] array){
        if(array.length == 0)
            return 0;
        int min  = array[0];
        for(int i = 1; i < array.length; i++){
            if(array[i] < min){
                min = array[i];
            }
        }
        return min;
    }
}
