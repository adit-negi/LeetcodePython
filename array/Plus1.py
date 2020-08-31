class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        for i in range(len(digits)):
            integer = integer + digits[i] * pow(10, len(digits)-1-i)
        integer = integer + 1
        integer = str(integer)
        if len(integer) != len(digits):
            digits.append(0)
        for i in range(len(integer)):

            digits[i] = integer[i]

        return digits
