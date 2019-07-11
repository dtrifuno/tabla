function fixId(obj) {
  const newObj = obj;
  newObj.id = newObj._id.$oid;
  delete newObj._id;
  return newObj;
}

export { fixId };
