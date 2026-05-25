class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # assertion: if all rows/columns are valid, board is valid

        # check rows
        for row in board:
            hashset = {}
            for value in row:
                if value != '.' and value not in hashset:
                    hashset[value] = 1
                elif value != '.':
                    return False
        # check columns
        for col in range(len(board)):
            hashset = {}
            for row in board:
                if row[col] != '.' and row[col] not in hashset:
                    hashset[row[col]] = 1
                elif row[col] != '.':
                    return False

        # check boxes
        # ranges = [[0,3], [3,6], [6,10]]
        for row in range(0,9,3):
            for col in range(0,9,3):
                hashset = {}

                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] != '.' and board[r][c] not in hashset:
                            hashset[board[r][c]] = 1
                        elif board[r][c] != '.':
                            return False
        
        return True


        """
        box one: i = {0, 3}, j = {0, 3}
        where i is the position range of each value in a row
        where j are the selected rows
        board[i][j]

        box one: i = {0, 3}, j = {0, 3}
        box two: i = {3, 6}, j = {0, 3}
        box three: i = {6, 10}, j = {0, 3}

        box four: i = {0, 3}, j = {3, 6}
        box five: i = {3, 6}, j = {3, 6}
        box six: i = {6, 10}, j = {3, 6}
        ...
        invariant: j so outer loop.
        """

        """
        iterate through each row first
        for each row, create the set of that row 
        the set will be the list of all keys in a hashset
        iterate through current row and update value as a counter of symbol
        row is valid iff hashset is all 1s
        """

        """
        compare each row at once.
        use an 'or' operation. 
        if any digit ends up as 1 then invalid
        """

        """
        each digit 1-9 has a unique bitmask 
        1 - 1
        2 - 10
        3 - 11
        4 - 100
        5 - 101
        6 - 110
        7 - 111
        8 - 1000
        """