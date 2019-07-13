import java.util.Stack;
public class Solution {
    private Stack<Integer> sdata = new Stack<Integer>();
    private Stack<Integer> smin= new Stack<Integer>();
    public void push(int node) {
        sdata.push(node);
        if(smin.isEmpty())
            smin.push(node);
        else{
            int min = smin.pop();
            smin.push(min);
            if(min < node){                
                smin.push(min);
            }else{
                smin.push(node);
            }
        }
    }
    
    public void pop() {
        if(!sdata.isEmpty()){
            sdata.pop();
            smin.pop();
        }
    }
    
    public int top() {
        int min = -1;
        if(!sdata.isEmpty()){
            min = sdata.pop();
            sdata.push(min);
        }        
        return  min;
    }
    
    public int min() {
        int min = -1;
        if(!smin.isEmpty()){
            min = smin.pop();
            smin.push(min);
        }
        return  min;
    }
}
