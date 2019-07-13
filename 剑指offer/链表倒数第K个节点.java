/*
 * public class ListNode {
 *     int val;
 *         ListNode next = null;
 *
 *             ListNode(int val) {
 *                     this.val = val;
 *                         }
 *                         }*/
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k) {
        int i = 0;
        ListNode curj = head;
        for(; i < k && curj != null; i++){
            curj = curj.next;
        }
        if(i < k)
            return null;
        ListNode curi = head;
        while(curj != null){
            curj = curj.next;
            curi = curi.next;
        }
        return curi;
    }
}
