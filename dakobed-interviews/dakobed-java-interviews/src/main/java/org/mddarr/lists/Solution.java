package org.mddarr.lists;

import java.util.HashSet;
import java.util.Set;

public class Solution {

    public void printList(ListNode head){
        
        ListNode current = head;
        while(current!= null){
            System.out.println(current.val);
            current = current.next;
        }
        
    }
    
    public ListNode reverseList(ListNode head){
        if(head == null)
            return null;
        ListNode prev = null;
        ListNode current = head;
        ListNode tmp;
        while(current != null){
            tmp = current.next;
            current.next = prev;
            prev = current;
            current = tmp;
        }
        return prev;   
    }

    public boolean hasCycle(ListNode head){
        Set<ListNode> nodesSeen = new HashSet<>();
        while(head!= null){
            if(nodesSeen.contains(head)){
                return true;
            }else{
                nodesSeen.add(head);
            }
            head = head.next;
        }
        return false;
    }

    public ListNode rotateRight(ListNode head, int k) {
        if(k ==0 || head == null || head.next == null)
            return head;
        ListNode current = head;
        int count = 0;
        while(current != null && current.next != null){
            count+=1;
            current = current.next;
        }
        ListNode last = current;
        current = head;
        int current_count = 0;
        System.out.println("k is count is " + k + " coount: " + count);
        if(k > count){
            k = k % count+1;
        }


        while(current_count < count-k){
            current_count+=1;
            current = current.next;
        }
        ListNode newhead = current.next;
        last.next = head;
        current.next = null;
        return newhead;
    }


}
