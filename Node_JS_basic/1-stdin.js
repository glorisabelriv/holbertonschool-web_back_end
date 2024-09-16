// Mostrar el mensaje inicial
console.log("Welcome to Holberton School, what is your name?");

// Leer la entrada estándar (stdin)
process.stdin.on('data', (input) => {
    const name = input.toString().trim(); // Convertir la entrada a string y eliminar espacios adicionales
    console.log(`Your name is: ${name}`); // Mostrar el nombre ingresado

    // Cerrar el programa y mostrar el mensaje final
    console.log("This important software is now closing");
    process.exit(); // Salir del programa
});
