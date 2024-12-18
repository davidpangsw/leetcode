class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # A "stack" by reusing prices
        # keep the stack strictly increasing
        st = [0]
        for i in range(1, len(prices)):
            while st and prices[i] <= prices[st[-1]]:
                top = st.pop()
                prices[top] -= prices[i]
            st.append(i)
        return prices

