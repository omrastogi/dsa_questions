from collections import defaultdict
from typing import List

# num_h, num_t and num_u are bound by 10, which effectively is constant-time
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = defaultdict(int)
        for digit in digits:
            freq[digit] += 1 
        uniq = sorted(freq.keys())
        arr = []
        for num_h in uniq:
            if num_h == 0:
                continue 
            for num_t in uniq:
                if num_h == num_t and freq[num_t] < 2:
                    continue 
                for num_u in uniq:
                    if num_u % 2 == 1: 
                        continue

                    if num_u == num_t or num_u == num_h:
                        if freq[num_u] < 2:
                            continue 
                        if num_u == num_t and num_u == num_h and freq[num_u] < 3:
                            continue 

                    arr.append(num_h*100 + num_t*10 + num_u)
        return arr
                    

if __name__ == "__main__":
    obj = Solution()
    digits = [2,1,3,0]
    print(obj.findEvenNumbers(digits))  # Expected: [102,120,130,132,210,230,302,310,312,320]
    
    digits = [2,2,8,8,2]
    print(obj.findEvenNumbers(digits))  # Expected: [222,228,282,288,822,828,882]
    
    digits = [3,7,5]
    print(obj.findEvenNumbers(digits))  # Expected: []

