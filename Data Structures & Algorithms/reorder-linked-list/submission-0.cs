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
    public void ReorderList(ListNode head) {

        // find middle for split 
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        } // slow.next will point at the start of the second half

        // reverse second half
        ListNode prev = null, curr = slow.next;
        slow.next = null; // remove second half from all list to create first half
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        // re-order
        ListNode first = head, second = prev;
        while (second != null) {
            ListNode tempFirst = first.next;
            ListNode tempSecond = second.next;

            first.next = second;
            second.next = tempFirst;

            first = tempFirst;
            second = tempSecond;
        }
    }
}
