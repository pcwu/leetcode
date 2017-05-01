/**
 * @param {string} path
 * @return {string}
 */

const simplifyPath = (path) => {
  const data = path.split('/').filter(text => text);
  const result = [];

  for (const word of data) {
    if (word === '..') {
      if (result.length > 0) {
        result.pop();
      }
    } else if (word !== '.') {
      result.push(word);
    }
  }
  return `/${result.join('/')}`;
};
