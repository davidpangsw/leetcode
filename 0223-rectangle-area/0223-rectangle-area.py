class Solution:
    def computeArea(self,
        ax1: int, ay1: int,
        ax2: int, ay2: int,
        bx1: int, by1: int,
        bx2: int, by2: int) -> int:

        total = (ax2-ax1) * (ay2-ay1) + (bx2-bx1) * (by2-by1)

        # find the overlap corners
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)
        # print(cx1, cy1, cx2, cy2)

        # if the overlap is possible, subtract the overlap area
        if (bx1 <= cx1 < bx2 and by1 <= cy1 < by2) and (bx1 < cx2 <= bx2 and by1 < cy2 <= by2):
            total -= (cx2-cx1) * (cy2-cy1) 
        return total