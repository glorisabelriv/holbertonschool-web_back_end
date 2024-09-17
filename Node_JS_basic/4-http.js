const http = require('http');

// Crear el servidor HTTP
const app = http.createServer((req, res) => {
  // Establecer el código de estado HTTP y el tipo de contenido
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  
  // Enviar la respuesta con el mensaje
  res.end('Hello Holberton School!');
});

// Hacer que el servidor escuche en el puerto 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exportar el servidor
module.exports = app;
