class Solution(object):
    def numComponents(self, head, nums):
        hashl = {}
        count = 0
        new = False
        for num in nums:
            hashl[num] = ''
        while head != None:
            if head.val not in hashl and new:
                new = False
            elif head.val in hashl and not new:
                new = True
                count = count + 1
            head = head.next
        return count
