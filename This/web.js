const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();
app.use(express.json());

const SECRET = 'supersecret'; // Weak secret!
let users = [];

// Register
app.post('/api/register', (req, res) => {
  const { email, password } = req.body;
  users.push({ email, password, role: 'user' });
  res.status(201).send({ message: 'User created' });
});

// Login
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  const user = users.find(u => u.email === email && u.password === password);
  if (!user) return res.status(401).send('Invalid credentials');
  const token = jwt.sign({ email: user.email, role: user.role }, SECRET);
  res.send({ token });
});

// Profile
app.get('/api/profile', (req, res) => {
  const token = req.headers.authorization?.split(' ')[1];
  try {
    const payload = jwt.verify(token, SECRET);
    res.send({ email: payload.email, role: payload.role });
  } catch (err) {
    res.status(401).send('Invalid token');
  }
});

// Admin Flag
app.get('/admin/flag', (req, res) => {
  const token = req.headers.authorization?.split(' ')[1];
  try {
    const payload = jwt.verify(token, SECRET);
    if (payload.role === 'admin') {
      res.send({ flag: 'CTF{jwt_weak_secret_123}' });
    } else {
      res.status(403).send('Admins only!');
    }
  } catch (err) {
    res.status(401).send('Invalid token');
  }
});

app.listen(3000, () => console.log('CTF API running on port 3000'));