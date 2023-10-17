class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)

        h = 0

        for i in range(len(citations)):
            if i+1 <= citations[i]:
                h+= 1
            else:
                break
        
        return h
