const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');
    lines.shift();

    console.log(`Number of students: ${lines.length}`);

    const fieldObj = {};
    for (const line of lines) {
      const fields = line.split(',');
      const field = fields[fields.length - 1];

      if (fieldObj[field]) {
        fieldObj[field] += 1;
      } else {
        fieldObj[field] = 1;
      }
    }

    for (const [field, count] of Object.entries(fieldObj)) {
      const st = lines.filter((line) => line.endsWith(field))
        .map((line) => line.split(',')[0])
        .join(', ');
      console.log(`Number of students in ${field}: ${count}. List: ${st}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
