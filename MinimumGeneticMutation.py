from collections import deque


class Solution(object):

    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1

        def valid_mutation(gene1, gene2):
            diff = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    diff += 1
                    if diff > 1:
                        return False

            return diff == 1

        bank = set(bank)
        visited = set()
        queue = deque([(startGene, 0)])

        while queue:
            current_gene, mutation = queue.popleft()
            visited.add(current_gene)

            if current_gene == endGene:
                return mutation

            for gene in bank:
                if gene not in visited and valid_mutation(current_gene, gene):
                    queue.append((gene, mutation+1))

        return -1
