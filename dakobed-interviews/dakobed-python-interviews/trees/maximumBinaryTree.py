class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.val)
        self.printInOrder(root.right)
    def constructMaximumBinaryTree(self, nums):
        return self.recursiveMaximumBinaryTree(nums)

    def recursiveMaximumBinaryTree(self, nums):
        if len(nums) ==0:
            return
        if len(nums) ==1:
            return TreeNode(nums[0])

        maxValue = float('-inf')
        indexMax = -1
        for i, num in enumerate(nums):
            if num > maxValue:
                maxValue = num
                indexMax = i
        node = TreeNode(maxValue)
        node.left = self.recursiveMaximumBinaryTree(nums[:indexMax])
        node.right = self.recursiveMaximumBinaryTree(nums[indexMax+1:])
        return node

nums = [3,2,1,6,0,5]
solution = Solution()
root = solution.constructMaximumBinaryTree(nums)
solution.printInOrder(root)