export default function updateUniqueItems(mapArg) {
  if (!(mapArg instanceof Map)) {
    throw new Error('Cannot process');
  }

  mapArg.forEach((value, key) => {
    if (value === 1) {
      mapArg.set(key, 100);
    }
  });

  return mapArg;
}
