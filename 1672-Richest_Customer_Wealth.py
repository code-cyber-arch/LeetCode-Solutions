class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_wealth = [None] * len(accounts)
        for i in range(len(accounts)):
            sum_wealth[i] = sum(accounts[i])
        return max(sum_wealth)
