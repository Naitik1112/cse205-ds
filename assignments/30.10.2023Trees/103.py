# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:return
        q=[root,None]
        ans,b,c=[],[],True
        while q:
            node=q.pop(0)
            if node is None:
                if not c:b=b[::-1]
                ans.append(b)
                b=[]
                c=not c
                if q:q.append(None)
                continue
            b.append(node.val)
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
        return ans