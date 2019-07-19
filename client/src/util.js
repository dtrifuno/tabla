/**
 * Returns a string of length or fewer characters. If the given stringer is
 * longer than length, it truncates and adds an ellipsis at the end.
 *
 * @param {string} str Input string
 * @param {number} length Max length of output string
 *
 * @return {string} String with length or fewer characters
 */
function shorten(str, length) {
  if (str.length <= length) {
    return str;
  }
  return `${str.slice(0, length - 3)}...`;
}

/**
 * Sorts an array of objects like a linked list by using the id and prev
 * properties.
 *
 * @param {Object[]} arr Array of objects that have prev and id properties
 *
 * @return {Object[]} A sorted deep copy of the array.
 */
function sortByPrev(arr) {
  const n = arr.length;
  const copy = JSON.parse(JSON.stringify(arr));

  // find head of list
  for (let i = 0; i < n; i += 1) {
    if (!copy[i].prev) {
      [copy[i], copy[0]] = [copy[0], copy[i]];
      break;
    }
  }

  // for each element put its sucessor after it
  for (let i = 0; i < n - 1; i += 1) {
    for (let j = i + 1; j < n; j += 1) {
      if (copy[j].prev === copy[i].id) {
        [copy[i + 1], copy[j]] = [copy[j], copy[i + 1]];
        break;
      }
    }
  }
  return copy;
}

/**
 * Returns a copy of an array of objects with an id property, setting
 * arr[i].prev = arr[i-1].id.
 *
 * @param {Object[]} arr An array of objects.
 *
 * @return {Object[]} A deep copy of the array with fixed prev properties.
 */
function prevFromOrder(arr) {
  const n = arr.length;
  if (n === 0) {
    return [];
  }
  const copy = JSON.parse(JSON.stringify(arr));
  copy[0].prev = null;

  for (let i = 1; i < n; i += 1) {
    copy[i].prev = copy[i - 1].id;
  }
  return copy;
}

/**
 * Returns an array of objects of newArr with different prev property
 * from those of oldArr (i.e. objects whose prev we need to update in the DB).
 *
 * @param {Object[]} arr The original array
 * @param {Object[]} newArr The new array
 *
 * @return {Object[]} Array of objects where prev differs between the two arrays
 */
function badPrevs(arr, newArr) {
  const objsToPut = [];
  for (let i = 0; i < arr.length; i += 1) {
    if (arr[i].prev !== newArr[i].prev) {
      objsToPut.push(newArr[i]);
    }
  }
  return objsToPut;
}

export { sortByPrev, prevFromOrder, badPrevs, shorten };
