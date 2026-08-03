/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public bool HasCycle(ListNode head) {
        ListNode p1 = head;
        ListNode p2 = head;

        while (p1 != null && p2 != null) {
            p1 = p1.next;
            if (p2.next != null) {
                p2 = p2.next.next;
            } else {
                return false;
            }

            if (p1 != null && p2 != null && p1.val == p2.val) {
                return true;
            }
        }
        return false;
    }
}
