class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if only one row or numRows >= length of s, just return s
        if numRows == 1 or numRows >= len(s):
            return s

        # Prepare a list of strings to represent each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        # Traverse each character in s, append to the current row
        for c in s:
            rows[cur_row] += c
            # If we reach top or bottom row, flip direction
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            cur_row += 1 if going_down else -1

        # Join all rows together and return
        return ''.join(rows)
