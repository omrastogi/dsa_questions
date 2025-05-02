class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        forces = [0] * N

        # Left to right (for 'R')
        force = 0
        for i in range(N):
            if dominoes[i] == 'R':
                force = N
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left (for 'L')
        force = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                force = N
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Final state
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        return ''.join(result)



if __name__ == "__main__":
    obj = Solution()
    dominoes = "RR.L"
    result = obj.pushDominoes(dominoes)
    print(f"Input: {dominoes}")
    print(f"Output: {result}")
