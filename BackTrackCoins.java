import java.util.Scanner;
import java.util.ArrayList;
public class BackTrackCoins {
    public static int[] coins = {1, 5, 10, 20, 50, 100};
    public static int ans = 0;
    
    public static void back(int remain, int depth, int[] coinNum, int preCoin, ArrayList<Integer> path)
    {
        if(remain == 0){
            ans += depth;
	    System.out.println(path);
	    System.out.println("depth="+depth);
        }else{
            for(int i = 0; i < 6; i++){
                 if(coinNum[i] > 0 && coins[i] >= preCoin && remain-coins[i] >= 0){
                     coinNum[i]--;
		     path.add(coins[i]);
                     back(remain-coins[i], depth+1, coinNum, coins[i], path);
		     path.remove(path.lastIndexOf(coins[i]));
                     coinNum[i]++;
                 }
            }
        }
    }
    
    public static String process(String num1, String num2)
    {
        String nums[] = num1.split(" ");
        int[] coinNum = new int[6];
        for(int i = 0; i < 6; i++){
            coinNum[i] = Integer.parseInt(nums[i]);
        }
        int total = Integer.parseInt(num2);
        back(total, 0, coinNum, 0, new ArrayList<Integer>());
        return ans+"";
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String strValueSequences = sc.nextLine();
        String strChargeNum = sc.nextLine();
        String sum = process(strValueSequences, strChargeNum);
        System.out.println(sum);
    }
}
