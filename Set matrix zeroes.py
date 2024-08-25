class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        fcol = False
        frow = False

        # check if anything in row 1 is zero
        for i in range(rows):
            if matrix[i][0]==0:
                fcol = True
        
        # check if anything in col 1 is zero
        for i in range(cols):
            if matrix[0][i]==0:
                frow = True

        # if any 0 set it's first row element and first col element to 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j]==0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # if any 0 in first, fill other too
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # if any 0 in first, fill other too
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        
        if fcol:
            for i in range(rows):
                matrix[i][0] = 0
        
        if frow:
            for i in range(cols):
                matrix[0][i] = 0
