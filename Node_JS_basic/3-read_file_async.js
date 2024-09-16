const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Leer el archivo de manera asíncrona
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        // Si hay un error, rechazamos la promesa
        reject(new Error('Cannot load the database'));
        return;
      }

      // Separar las líneas del archivo y eliminar líneas vacías
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
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

      // Resolver la promesa al final
      resolve();
    });
  });
}

module.exports = countStudents;
