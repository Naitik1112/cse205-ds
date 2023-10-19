class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)

        for i in range(n):
            # Assume the current index is the minimum
            min_index = i

            # Find the minimum element in the unsorted part
            for j in range(i + 1, n):
                if prices[j] < prices[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element
            prices[i], prices[min_index] = prices[min_index], prices[i]
        
       
        m = prices[0] + prices[1]
        if money - m >= 0 :
            return money - m 
        else:
            return money      
