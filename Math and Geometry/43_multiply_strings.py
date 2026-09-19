class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10
        res = "".join(map(str, result)).lstrip("0")
        return res


sol = Solution()
assert sol.multiply("2", "3") == "6"
assert sol.multiply("123", "456") == "56088"
assert sol.multiply("0", "52") == "0"
print("All tests passed")
