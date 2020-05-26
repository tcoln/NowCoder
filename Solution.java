import org.omg.PortableInterceptor.INACTIVE;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    class Node{
        int val;
        Node left;
        Node right;
        public Node(int val){
            this.val = val;
        }
    }

    private Node createBinaryTreeByArray(Integer[] array,int index)
    {
        Node tn = null;
        if (index<array.length) {
            Integer value = array[index];
            if (value == null) {
                return null;
            }
            tn = new Node(value);
            tn.left = createBinaryTreeByArray(array, 2*index+1);
            tn.right = createBinaryTreeByArray(array, 2*index+2);
            return tn;
        }
        return tn;
    }

    public int levelOrder(Node root){
        int ave = 0;
        List<Node> nextl = new LinkedList<Node>();
        List<Node> curl = new LinkedList<Node>();
        curl.add(root);
        double max = 0;
        int maxL = 0;
        int level = 0;
        while(curl.length > 0 && nextl.length > 0){            
            int n = 0;
            double ave = 0;            
            while(curl.hasNext()){
                Node cur = curl.get(0);
                curl.removeFirst();
                nextl.add(cur.left);
                nextl.add(cur.right);
                n += 1;
                ave += cur.val;
            }
            level += 1;
            curl = nextl;
            nextl = new LinkedList<Node>();
            ave = ave / n;
            if(ave >= max){
                maxL = level;
                max = ave;
            }
        }
    }


    public  Node createTree(int[] array){
        List<Node> nodeList=new LinkedList<Node>();

        for(int nodeIndex=0;nodeIndex<array.length;nodeIndex++){
            nodeList.add(new Node(array[nodeIndex]));
        }
        for(int parentIndex=0;parentIndex<=array.length/2-1;parentIndex++){
            nodeList.get(parentIndex).left =nodeList.get(parentIndex*2+1);
            if((parentIndex*2+2)<array.length) {
                nodeList.get(parentIndex).right = nodeList.get(parentIndex * 2 + 2);
            }
        }
        return nodeList.get(0);
    }


    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer [] array = new Integer[n];
        for(int i = 0;i < n;i++){
            String value =scanner.next();
            if(value.equals( "null" )){
                array[i]=null;
            }else{
                array[i] = Integer.valueOf( value );
            }

        }
        Solution solution = new Solution ();
        Node root =solution.createBinaryTreeByArray(array,0);
        int level = solution.levelOrder( root );
        System.out.println(level);
    }
}
