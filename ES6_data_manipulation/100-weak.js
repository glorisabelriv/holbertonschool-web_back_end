// Exporta una instancia de WeakMap llamada weakMap
export const weakMap = new WeakMap();

// Exporta la función queryAPI
export function queryAPI(endpoint) {
  if (!weakMap.has(endpoint)) {
    // Si el endpoint no está en el WeakMap, se inicializa con 0
    weakMap.set(endpoint, 0);
  }

  // Incrementa el contador para el endpoint dado
  let count = weakMap.get(endpoint);
  count += 1;
  weakMap.set(endpoint, count);

  // Si el contador es mayor o igual a 5, lanza un error
  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }
}
