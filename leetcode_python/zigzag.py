# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # initialize a matrix with numRows * empty strings
        matrix = [""]*numRows
        # default moving direction, down
        inc = 1
        # i is the index of row in the matrix
        i = 0
        for x in range(len(s)):
            # append char in s to corresponding row of matrix
            matrix[i] += s[x]
            # if out of boundary, change moving direction
            if i+inc >=numRows or i+inc < 0:
                inc = -inc
            i += inc
        # append each strings in matrix to the result string     
        res = ""
        for ma in matrix:
            res += ma
        return res