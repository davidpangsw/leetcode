class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # keep the stack strictly increasing
        st = [0]
        for i in range(1, len(prices)):
            while st and prices[i] <= prices[st[-1]]:
                prices[st.pop()] -= prices[i]
            st.append(i)
        return prices

