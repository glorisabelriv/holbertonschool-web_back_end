export default function getListStudents() {
  return [
    {
      id: 1,
      firstName: "Guillaume",
      location: "San Francisco",
    },
    {
      id: 2,
      firstName: "James",
      location: "Columbia",
    },
    {
      id: 5,
      firstName: "Serena",
      location: "San Francisco",
    },
  ];
}

// Llamada a la función y salida en la consola
console.log(getListStudents());
