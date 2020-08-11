package org.mddarr.trees;

public class BinaryTreeProblems {
    public static void main(String[] args){
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        Solution solution = new Solution();
        solution.printTree(root);
//        System.out.println("The sum of the left leaves is " + solution.sumOfLeftLeaves(root));
    }



}
