package org.mddarr.trees;

import com.sun.source.tree.Tree;

public class BinaryTreeProblems {
    public static void main(String[] args){
//        TreeNode root = new TreeNode(3);
//        root.left = new TreeNode(9);
//        root.right = new TreeNode(20);
//        root.right.left = new TreeNode(15);
//        root.right.right = new TreeNode(7);
        Solution solution = new Solution();
//        solution.printTree(root);

        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(3);
        root1.right = new TreeNode(2);
        root1.left.left = new TreeNode(5);

        TreeNode root2 = new TreeNode(2);
        root2.left = new TreeNode(1);
        root2.right = new TreeNode(3);
        root2.left.right = new TreeNode(4);
        root2.right.right = new TreeNode(7);

        TreeNode root3 = solution.mergeTrees(root1, root2);
//        solution.printPreOrder(root3);

        int val = root3.left.val;
        System.out.println("The value " + val);

    }



}
