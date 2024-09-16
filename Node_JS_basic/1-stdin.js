const os = require('os'); // Importa el módulo os para manejar el salto de línea apropiado

// Mostrar el mensaje inicial
console.log(`Welcome to Holberton School, what is your name?${os.EOL}`);

// Leer la entrada estándar (stdin)
process.stdin.on('data', (input) => {
    const name = input.toString().trim(); // Convertir la entrada a string y eliminar espacios adicionales
    console.log(`Your name is: ${name}${os.EOL}`); // Mostrar el nombre ingresado

    // Cerrar el programa y mostrar el mensaje final
    console.log(`This important software is now closing${os.EOL}`);
    process.exit(); // Salir del programa
});
