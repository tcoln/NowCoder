import java.util.ArrayList;
public class Solution {

    public static void main(String[] args){
	Solution s = new Solution();
	int [] a = {6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335};
	int [] b = {12,13,14,1,2,3,4};
	System.out.println(s.minNumberInRotateArray(a));
	System.out.println(s.minNumberInRotateArray(b));
    }

    public int minNumberInRotateArray(int [] array) {
        int l = array.length;
        if(l == 0)
            return 0;
        int s = 0;
        int e = l - 1;
        while(s < e){
            int m = (s + e) / 2;
            System.out.println(s + " " + e + " " + m);
            System.out.println(array[s] + " " + array[e] + " " + array[m]);
            if(array[m] > array[s])
                s = m + 1;
            else if(array[m] < array[s])
                e = m;
            else if(array[m] == array[s] && s + 1 == e)
		s = e;
                break;
        }
        return array[s];
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
