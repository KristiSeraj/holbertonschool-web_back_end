export default function hasValuesFromArray(set, arr) {
  return arr.every((el) => set.has(el));
}
