public class Solution {
    public void reOrderArray(int [] array) {
        int oddi = 0;
        int eveni = 0; // pos of first even number
        int l = array.length;
        int odd[] = new int[l];
        int even[] = new int[l];
        for(int i = 0; i < l; i++){
            if(array[i] % 2 == 1)
                odd[oddi++] = array[i];
            else
                even[eveni++] = array[i];
        }
        for(int i = 0; i < oddi; i++)
            array[i] = odd[i];
        for(int i = 0; i < eveni; i++)
            array[oddi+i] = even[i];
    }
}
