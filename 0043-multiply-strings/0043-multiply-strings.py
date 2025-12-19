class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # Multiply digits from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10

        # Convert result to string, skipping leading zeros
        result = []
        for digit in res:
            if not result and digit == 0:
                continue
            result.append(str(digit))

        return "".join(result) if result else "0"
