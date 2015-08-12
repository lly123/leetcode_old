__author__ = 'richard'

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes
# v and w as the lowest node in T that has both v and w as descendants
# (where we allow a node to be a descendant of itself)."

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}

    def lowestCommonAncestor(self, root, p, q):
        def search(t, p, q):
            found_p = False
            found_q = False
            if t is p:
                found_p = True
            if t is q:
                found_q = True
            if found_p and found_q:
                return True, True, t
            else:
                b1, b2, n1 = search(t.left, p, q) if t.left else (False, False, None)
                if b1 and b2:
                    return True, True, n1
                b3, b4, n2 = search(t.right, p, q) if t.right else (False, False, None)
                if b3 and b4:
                    return True, True, n2
                if (found_p or b1 or b3) and (found_q or b2 or b4):
                    return True, True, t
                return found_p or b1 or b3, found_q or b2 or b4, None
        return search(root, p, q)[2]


# t1 = TreeNode(10)
# t2 = TreeNode(12)
# t3 = TreeNode(15)
# t4 = TreeNode(20)
# t5 = TreeNode(30)
#
# t3.left = t2
# t3.right = t4
# t2.left = t1
# t2.right = t5
#
# print(Solution().lowestCommonAncestor(t3, t1, t2).val)
