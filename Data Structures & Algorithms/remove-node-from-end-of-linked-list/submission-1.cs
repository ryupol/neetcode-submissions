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
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        if (head.next == null) return null;

        ListNode node = new ListNode(0, head);
        ListNode first = node.next, second = node;
        while (first != null) {
            if (n > 0) {
                first = first.next;
                n--;
            } else {
                first = first.next;
                second = second.next;
            }
        }
        second.next = second.next.next;

        return node.next;
    }
}
