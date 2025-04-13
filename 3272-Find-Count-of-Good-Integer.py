from math import factorial
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def generate_palindromes(n):
            half = (n + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for num in range(start, end):
                s = str(num)
                if n % 2 == 0:
                    yield int(s + s[::-1])
                else:
                    yield int(s + s[-2::-1])

        def count_permutations(s):
            cnt = Counter(s)
            total = factorial(len(s))
            for v in cnt.values():
                total //= factorial(v)
            # Subtract permutations with leading zero
            if cnt['0']:
                cnt['0'] -= 1
                total -= factorial(len(s) - 1) // (
                    factorial(cnt['0']) * 
                    prod(factorial(cnt[d]) for d in cnt if d != '0')
                )
                cnt['0'] += 1
            return total

        def prod(iterable):
            result = 1
            for x in iterable:
                result *= x
            return result

        seen = set()
        result = 0
        for p in generate_palindromes(n):
            if p % k != 0:
                continue
            key = ''.join(sorted(str(p)))
            if key in seen:
                continue
            seen.add(key)
            result += count_permutations(key)
        return result

if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 9
    print(sol.countGoodIntegers(n, k))
