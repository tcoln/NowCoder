public class Solution {
    public int NumberOf1(int n) {
        int ans = 0;
        while(n!=0){
            ans += 1;
            n = n&(n-1);
        }
        return ans;
    }
}
