package org.mddarr.trees;

public class Solution {
    int sum = 0;
    public int sumOfLeftLeaves(TreeNode root){
        if(root == null){
            return 0;
        }
        findSum(root, -1);
        return sum;
    }

    public void printTree(TreeNode root){
        if(root == null)
            return;
        printTree(root.left);
        System.out.println(root.val);
        printTree(root.right);
    }

    public void findSum(TreeNode root, int direction){
        if(root == null)
            return;
        if(root.left == null && root.right == null){
            if(direction ==0){
                sum += root.val;
            }
            findSum(root.left, 0);
            findSum(root.right, 1);
        }
    }
}
