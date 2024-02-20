from typing import List

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         max_area = 0
#         st = [] # store [height, index, area]
#         # rule of st is that it should be increasing always
#         for i, h in enumerate(heights): 
#             if not st:
#                 st.append([h, i, heights])
#                 continue
#             print("status", st, h)
#             if st[-1][0] > h:
#                 for i in range(len(st)):
#                     if st[-1][0] > h:
#                         print("popn", st)
#                         _,_,area = st.pop()
#                         max_area = max(area, max_area)

#                 for s in st:
#                     print("addin height", s)
#                     s[2]+=s[0] # its own height is added to the area
#                 a = h 
#                 print(heights[st[-1][1] : i+1], st[-1][1], i)
#                 for k in heights[st[-1][1]: i+1][::-1]:      
#                     if k > h:
#                         a+=h
#                     else:
#                         break 

#                 st.append([h, i, a])
#                 print("addn", [h,a])
#             else:
#                 for s in st:
#                     print("addin height", s)
#                     s[2]+=s[0] # its own height is added to the area
#                 st.append([h, i, h])
            
#         print("final stack",st)
#         for s in st:
#             max_area = max(s[2], max_area)

#         return max_area
                
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stack stores indices of heights in increasing order

        for i, h in enumerate(heights + [0]):  # Append 0 to handle remaining elements in stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area


if __name__ == "__main__":
    obj = Solution()
    a = [3,6,5,7,4,8,1,0]
    # a = [2,1,2]
    print(obj.largestRectangleArea(a))
