export function getFeatureCenter(feature) {
  if (!feature || !feature.geometry) return null;
  const coords = feature.geometry.coordinates;
  if (feature.geometry.type === 'Point') return coords.slice().reverse();
  let lat = 0, lng = 0, count = 0;
  function traverse(arr) {
    if (typeof arr[0] === 'number') {
      lng += arr[0];
      lat += arr[1];
      count++;
    } else {
      arr.forEach(traverse);
    }
  }
  traverse(coords);
  return count ? [lat / count, lng / count] : null;
}
