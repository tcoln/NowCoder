import java.util.Stack;
public class Solution {
    Stack<Integer> s = new Stack<Integer>();
    Stack<Integer> smin = new Stack<Integer>();
    public void push(int node) {
        s.push(node);
        if(smin.pop() < node)
            smin.push(smin.pop());
        else
            smin.push(node);
    }
    
    public void pop() {
        s.pop();
        smin.pop();
    }
    
    public int top() {
        return s.pop();
    }
    
    public int min() {
        return smin.pop();
    }
}
