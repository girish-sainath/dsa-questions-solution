from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with infinity (impossible state)
        # dp[i] = minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # Fill dp array for each amount from 1 to amount
        for current_amount in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                # If coin value <= current amount, we can use this coin
                if coin <= current_amount:
                    # Update dp[current_amount] if using this coin gives better result
                    # dp[current_amount - coin] + 1 means:
                    #   use 1 coin of 'coin' denomination +
                    #   minimum coins needed for remaining amount
                    dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
        
        # If dp[amount] is still infinity, amount cannot be made up
        return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: coins = [1,2,5], amount = 11
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = solution.coinChange(coins1, amount1)
    print(f"Test 1: coins={coins1}, amount={amount1}")
    print(f"Output: {result1}")  # Expected: 3
    print()
    
    # Test Case 2: coins = [2], amount = 3
    coins2 = [2]
    amount2 = 3
    result2 = solution.coinChange(coins2, amount2)
    print(f"Test 2: coins={coins2}, amount={amount2}")
    print(f"Output: {result2}")  # Expected: -1
    print()
    
    # Test Case 3: coins = [1], amount = 0
    coins3 = [1]
    amount3 = 0
    result3 = solution.coinChange(coins3, amount3)
    print(f"Test 3: coins={coins3}, amount={amount3}")
    print(f"Output: {result3}")  # Expected: 0