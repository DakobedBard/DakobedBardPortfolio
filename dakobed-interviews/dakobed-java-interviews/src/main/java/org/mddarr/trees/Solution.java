package org.mddarr.trees;

import java.util.Stack;

public class Solution {
    int sum ;

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2){
        if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }

    public TreeNode mergeTreesIterative(TreeNode t1, TreeNode t2){
        if(t1 == null)
            return t2;
        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[]{t1, t2});
        while(!stack.isEmpty()){
            TreeNode[] t = stack.pop();
            if(t[0] == null || t[1] == null){
                continue;
            }
            t[0].val += t[1].val;
            if(t[0].left == null){
                t[0].left = t[1].left;
            }else{
                stack.push(new TreeNode[] {t[0].left, t[1].left});
            }
            if(t[0].right == null){
                t[0].right = t[1].right;
            }else{
                stack.push(new TreeNode[] {t[0], t[1].right });
            }
        }
        return t1;
    }

    public int sumOfLeftLeaves(TreeNode root){
        sum = 0;
        if(root == null){
            return 0;
        }
        findSum(root, -1);
        return sum;
    }

    public void findSum(TreeNode root, int direction){
        if(root == null){
            return;
        }
        if(root.left == null && root.right == null){
            if(direction ==0){
                sum += root.val;
            }
        }
        findSum(root.left, 0);
        findSum(root.right, 1);
    }

    public void printTree(TreeNode root){
        if(root == null)
            return;
        printTree(root.left);
        System.out.println(root.val);
        printTree(root.right);
    }

    public void printPreOrder(TreeNode root){
        if(root == null)
            return;
        System.out.println(root.val);
        printTree(root.left);
        printTree(root.right);
    }


}
