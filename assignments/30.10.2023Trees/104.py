class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue=[root]
        level=1
        while queue:
            next_queue=[]
            for i in queue:
                if i.left: next_queue.append(i.left)
                if i.right: next_queue.append(i.right)
            queue=next_queue
            level+=1
        return level-1