def get_sum(n):
    out_list = []
    power = 1
    sumation = 0
    while n>0:
        sumation += (n%(10**power))**2
        n = n // 10
    return sumation

class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        for _ in range(10+n):
            n = get_sum(n)
            if n in memo:
                return False 
            elif n == 1:
                return True 
            else:
                memo.add(n)
        return False

if __name__ == "__main__":
    sol = Solution()
    test_cases = [19, 2, 30]
    for n in test_cases:
        print(f"Is {n} a happy number? {sol.isHappy(n)}")