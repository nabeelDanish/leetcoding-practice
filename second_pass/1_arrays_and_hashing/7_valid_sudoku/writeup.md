# Valid Sudoku

A medium leetcode problem but is actually pretty simple to solve

## Solution 1 - Hashmaps
The idea for the correct sudoku is that no number repeats in all the 9 rows, columns, and boxes. So we simply need 9 hashmaps for all the rows, 9 hashmaps for all the columns, and 9 hashmaps for all the boxes. These hashmaps can be placed inside a list

We iterate over the board, from `i -> 9, j -> 9`, and first check whether or not the character we have at at `board[i][j]` is a number. If it is a number we proceed forward

Now, given the `(i, j)` position, the only tricky part is to find the right hashmap for the rows, columns, and the boxes. 

For the rows, it is simply `rows[i]` and for the columns it is simply `columns[j]`. For the boxes, if we assume that boxes are indexed `0-8` from top left to bottom right, in that order, than the formula for computing the box index is `index = (i // 3) * 3 + (j // 3)`

Notice the use of `//` to make sure that we get truncated integer division (example `5 // 3 == 1`)

This gives us the following solution:
```
rows = [{} for _ in range(9)]
columns = [{} for _ in range(9)]
boxes = [{} for _ in range(9)]

for i in range(9):
    for j in range(9):
        num = board[i][j]
        if not num.isdigit():
            continue

        if num in rows[i]:
            return False
        if num in columns[j]:
            return False
        if num in boxes[(i // 3) * 3 + (j // 3)]:
            return False

        rows[i][num] = True
        columns[j][num] = True
        boxes[(i // 3) * 3 + (j // 3)][num] = True

return True
```

### Complexity Analysis
The time complexity of this solution is `O(9 * 9) => O(18) => O(1)` and the space complexity of this problem is `O(9 + 9 + 9) => O(27) => O(1)`