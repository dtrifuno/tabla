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

async function promiseForEach(arr, fn) {
  for (const item of arr) await fn(item);
}

export { sortByPrev, prevFromOrder, promiseForEach };
