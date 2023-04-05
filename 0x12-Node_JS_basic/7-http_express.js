const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');
  try {
    const data = await countStudents(process.argv[2]);
    res.end(`${data.join('\n')}`);
  } catch (error) {
    res.end(error.message);
  }
});

app.listen(1245);

module.exports = app;
