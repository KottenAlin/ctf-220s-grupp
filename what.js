const express = require("express");
const app = express();

app.use(express.json());

app.post("/eval", (req, res) => {
    const userInput = req.body.input;

    try {
        // Insecure use of eval
        const result = eval(userInput);
        res.send(`Result: ${result}`);
    } catch (err) {
        res.status(400).send("Error: Invalid input");
    }
});

app.listen(3000, () => {
    console.log("CTF challenge running on http://localhost:3000");
});
