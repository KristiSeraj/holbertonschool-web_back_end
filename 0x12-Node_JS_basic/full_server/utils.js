const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error(err));
      } else {
        const lines = data.trim().split('\n');
        lines.shift();
        const students = [];
        
        for (const line of lines) {
          const fields = line.split(',');
          const fieldObj = {
            firstName: fields[0],
            field: fields[fields.length - 1],
          };
          students.push(fieldObj);
        }
        
        const result = students.reduce((acc, student) => {
          if (!acc[student.field]) {
            acc[student.field] = [];
          }
          acc[student.field].push(student.firstName);
          return acc;
        }, {});
        
        resolve(result);
      }
    })
  })
}


export default readDatabase;
