st=[None]*(100001)
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ret=inf
        # st=deque([(0,-1)])
        st[0]=(0,-1)
        cur=l=r=0
        # for i,num in enumerate(nums,2):
        for i in range(n):
            cur+=nums[i]
            if nums[i]>0:
                tmp=None
                # while st and cur-st[0][0]>=k:
                #     tmp=st[0][1]
                #     st.popleft()
                while l<=r and cur-st[l][0]>=k:
                    # if i-st[l][1]<ret:ret=i-st[l][1]
                    tmp=st[l][1]
                    l+=1
                # print(tmp,i-tmp,ret)
                if tmp is not None and i-tmp<ret:ret=i-tmp
            else:
                # while st and cur<=st[-1][0]:st.pop()
                while r>=l and cur<=st[r][0]:r-=1
            
            # st.append((cur,i))
            r+=1
            st[r]=(cur,i)

        return ret if ret!=inf else -1