# Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        transactions = []   # [(profit, buyPrice, sellPrice)]
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                transactions.append((prices[i] - prices[i-1], prices[i-1], prices[i]))

        if len(transactions) <= k:
            return sum([t[0] for t in transactions]) if len(transactions) > 0 else 0

        mergeCost = [transactions[i][1] - transactions[i-1][2] for i in range(1, len(transactions))]    # cost if merging transactions[i] and transactions[i+1]

        while len(transactions) > k:
            # Drop transaction
            if -(min(transactions)[0]) >= max(mergeCost):
                idxMin = transactions.index(min(transactions))
                if idxMin == 0:
                    transactions.pop(0)
                    mergeCost.pop(0)
                elif idxMin == len(transactions)-1:
                    transactions.pop(idxMin)
                    mergeCost.pop(idxMin-1)
                else:
                    transactions.pop(idxMin)
                    mergeCost.pop(idxMin)
                    mergeCost[idxMin-1] = transactions[idxMin][1] - transactions[idxMin-1][2]
            # Merge transaction
            else:
                idxMin = mergeCost.index(max(mergeCost))
                mergeCost.pop(idxMin)
                transactions[idxMin] = (transactions[idxMin+1][2]-transactions[idxMin][1], transactions[idxMin][1], transactions[idxMin+1][2])
                transactions.pop(idxMin+1)
        
        return sum([t[0] for t in transactions])
