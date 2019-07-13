function fixId(obj) {
  const newObj = obj;
  newObj.id = newObj._id.$oid;
  delete newObj._id;
  return newObj;
}

function sortByOrder(arr) {
  const newArr = JSON.parse(JSON.stringify(arr));
  newArr.sort((x, y) => x.order - y.order);
  return newArr;
}

function sortById(arr) {
  const newArr = JSON.parse(JSON.stringify(arr));
  newArr.sort((x, y) => x.id - y.id);
  return newArr;
}

function orderFromPosition(arr) {
  let order = 0;
  const newArr = [];
  arr.forEach((obj) => {
    const newObj = {
      ...obj,
      order,
    };
    newArr.push(newObj);
    order += 1;
  });
  return newArr;
}

export {
 fixId, sortByOrder, orderFromPosition, sortById 
};
