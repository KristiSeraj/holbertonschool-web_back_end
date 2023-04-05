const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const rsp = [];
        let msg;
        const lines = data.trim().split('\n');
        lines.shift();
        msg = `Number of students: ${lines.length}`;
        console.log(`Number of students: ${lines.length}`);
        rsp.push(msg);

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
          msg = `Number of students in ${field}: ${count}. List: ${st}`;
          console.log(`Number of students in ${field}: ${count}. List: ${st}`);
          rsp.push(msg);
        }
        resolve(rsp);
      }
    });
  });
}

module.exports = countStudents;
