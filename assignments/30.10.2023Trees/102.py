# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]
        if root!=None:
            q.append(root)

        while len(q)>0:
            level=[]
            qlen=len(q)

            for _ in range(qlen):
                node=q.popleft()
                level.append(node.val)
                if node.left!=None:
                    q.append(node.left)

                if node.right!=None:
                    q.append(node.right)


            ans.append(level)

        return ans