const http = require('http');
const countStudents = require('./3-read_file_async');

// Recuperar el argumento de la línea de comandos (nombre del archivo CSV)
const databaseFile = process.argv[2];

// Crear el servidor HTTP
const app = http.createServer((req, res) => {
  // Configurar la cabecera de respuesta para texto plano
  res.setHeader('Content-Type', 'text/plain');

  // Ruta raíz '/'
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  }

  // Ruta '/students'
  else if (req.url === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');

    // Llamar a countStudents para obtener la lista de estudiantes
    countStudents(databaseFile)
      .then(() => {
        res.end(); // Finalizar la respuesta una vez que se hayan mostrado los estudiantes
      })
      .catch((error) => {
        res.statusCode = 500;
        res.end(error.message); // Mostrar el mensaje de error en caso de fallo
      });
  }

  // Cualquier otra ruta
  else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

// Hacer que el servidor escuche en el puerto 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exportar el servidor
module.exports = app;
