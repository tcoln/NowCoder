public class Solution {
    public int JumpFloor(int target) {
        if(target <= 2)
            return target;
        int ans[] = new int[target];
        ans[0] = 1;
        ans[1] = 2;
        for(int i = 2; i < target; i++)
            ans[i] = ans[i-1] + ans[i-2];
        return ans[target-1];
    }
}
