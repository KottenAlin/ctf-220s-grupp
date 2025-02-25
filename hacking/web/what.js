const fs = require('fs');

// Dangerous: Using eval to access the file system
let userInput = "fs.readdirSync('.')";  // List files in the current directory
let result = eval(userInput);
console.log(result);