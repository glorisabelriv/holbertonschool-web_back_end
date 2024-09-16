const fs = require('fs');

function countStudents(path) {
  try {
    // Leer el archivo de manera síncrona
    const data = fs.readFileSync(path, 'utf8');

    // Separar las líneas del archivo
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Eliminar líneas vacías

    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Eliminar la primera línea (cabecera)
    const students = lines.slice(1);

    // Contar el número total de estudiantes
    console.log(`Number of students: ${students.length}`);

    // Crear un objeto para contar estudiantes por campo
    const fields = {};

    // Iterar sobre cada estudiante
    students.forEach((line) => {
      const [firstname, , , field] = line.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname); // Añadir el nombre del estudiante a su campo
    });

    // Mostrar la cantidad de estudiantes por campo y la lista de nombres
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      }
    }

  } catch (error) {
    // Si ocurre un error, lanzar el mensaje de error requerido
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
