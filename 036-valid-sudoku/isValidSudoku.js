/**
 * @param {character[][]} board
 * @return {boolean}
 */
const isValidSudoku = (board) => {
  for (let i = 0; i < 9; i += 1) {
    const row = {};
    const col = {};
    const block = {};
    for (let j = 0; j < 9; j += 1) {
      if (row[board[i][j]] !== undefined || col[board[j][i]] !== undefined) {
        return false;
      }
      if (block[Math.trunc(i / 3)][Math.trunc(j / 3)][board[i][j]] !== undefined) {
        return false;
      }
      if (board[i][j] !== '.') {
        row[board[i][j]] = true;
      }
      if (board[j][i] !== '.') {
        col[board[j][i]] = true;
      }
      if (board[i][j] !== '.') {
        block[Math.trunc(i / 3)][Math.trunc(j / 3)][board[j][i]] = true;
      }
    }
  }
  return true;
};
