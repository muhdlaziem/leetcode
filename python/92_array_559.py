def solve(digits: list[int], cur: int, last):
    # print(1, digits, cur, last)
    if last % 10 == 0:
        new_cur = cur-1
        digits[cur] = last % 10
        if new_cur == -1:
            # print(f"hi {last/10}")
            digits.insert(0, int((last / 10)))
            # print(f"result = {digits}")
        else:
            digits[new_cur] = int(digits[new_cur] + (last / 10))
        # print(2, digits, cur, last)
        return solve(digits=digits, cur=new_cur, last=digits[new_cur])

    digits[cur] = last
    return digits


class Solution(object):
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cur = len(digits)-1
        last = digits[cur] + 1
        return solve(digits, len(digits)-1, last=last)


a = Solution()
print(a.plusOne([9, 9, 9]) == [1, 0, 0, 0])
print(a.plusOne([1, 2, 3]) == [1, 2, 4])
print(a.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2])
print(a.plusOne([9]) == [1, 0])
