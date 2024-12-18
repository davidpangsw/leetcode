class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # A "stack" by reusing prices
        # keep the stack strictly increasing
        st = []
        for i in range(len(prices)):
            while st and prices[i] <= prices[st[-1]]:
                top = st.pop()
                prices[top] -= prices[i]
            st.append(i)
        return prices

