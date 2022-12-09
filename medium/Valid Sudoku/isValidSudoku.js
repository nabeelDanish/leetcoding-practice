/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  const rowMaps = [];
  const columnMaps = [];
  const boxMaps = [];

  // Creating a list of hashmaps
  for (let i = 0; i < 9; ++i) {
    rowMaps.push({});
    columnMaps.push({});
    boxMaps.push({});
  }

  // Iterating over the board
  for (let i = 0; i < board.length; ++i) {
    const row = board[i];
    for (let j = 0; j < row.length; ++j) {
      const n = row[j];

      if (n == ".") continue;

      // Checking Row Condition
      if (rowMaps[i][n] != null) {
        return false;
      } else {
        rowMaps[i][n] = true;
      }

      // Checking Column Condition
      if (columnMaps[j][n] != null) {
        return false;
      } else {
        columnMaps[j][n] = true;
      }

      // Checking Box Map
      const boxIndex = 3 * Math.floor(i / 3) + Math.floor(j / 3);
      if (boxMaps[boxIndex][n] != null) {
        return false;
      } else {
        boxMaps[boxIndex][n] = true;
      }
    }
  }

  return true;
};

const testIsValidSudoku = function (board, output) {
  const result = isValidSudoku(board);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: board: ${JSON.stringify(
        board
      )} output: ${output} result: ${result}`
    );
  }
};

testIsValidSudoku(
  [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ],
  true
);

testIsValidSudoku(
  [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ],
  false
);
