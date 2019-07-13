/**
 * public class TreeNode {
 *     int val = 0;
 *         TreeNode left = null;
 *             TreeNode right = null;
 *
 *                 public TreeNode(int val) {
 *                         this.val = val;
 *
 *                             }
 *
 *                             }
 *                             */
public class Solution {
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if(root1 == null || root2 == null) // important
            return false;
        if(IsSame(root1, root2))
            return true;
        if(HasSubtree(root1.left, root2))
            return true;
        if(HasSubtree(root1.right, root2))
            return true;
        return false;
    }
    
    public boolean IsSame(TreeNode r1, TreeNode r2){
        boolean same = false;
        if(r2 == null)
            return true;
        if(r1 == null)
            return false;
        else if(r1.val == r2.val){
            System.out.println(r1.val + ' ' + r2.val);
            same = IsSame(r1.left, r2.left) && IsSame(r1.right, r2.right);
        }
        return same;
    }
}
