public class Solution {
    public String replaceSpace(StringBuffer str) {
    	String ans = "";
        ans = str.toString().replace(" ", "%20");
        int l = str.length();
        for(int i = 0; i < l; i++){
            char c = str.charAt(i);
            if(c == ' ')
                ans += "%20";
            else
                ans += c;
        }
        return ans;
    }
}
