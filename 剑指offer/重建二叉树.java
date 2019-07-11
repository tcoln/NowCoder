// Definition for binary tree
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        return constructTree(pre, 0, pre.length-1, in, 0, in.length-1);
    }
    
    public TreeNode constructTree(int [] pre, int pres, int pree, int [] in, int ins, int ine){
        if(pres > pree || ins > ine){
            return null;
        }
        TreeNode h = new TreeNode(pre[pres]);
        int pos = ins;
        while(in[pos] != pre[pres]){
            pos += 1;
        }
        h.left = constructTree(pre, pres+1, pres+(pos-ins), in, ins, pos-1);
        h.right = constructTree(pre, pres+(pos-ins)+1, pree, in, pos+1, ine);
        return h;
    }
    
    public static void main(String argv[]){
	Solution s = new Solution();
	s.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
    }
}


