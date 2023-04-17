const readDatabase = require('../utils');

export default class StudentController {
  static getAllStudents(request, response, db) {
    readDatabase(db)
    .then((fields) => {
      const students = [];
      let message;

      for (const key of Object.keys(fields)) {
        message = `Number of students in ${key}: ${fields[key].length}. List ${fields[key].join(', ')}`;
        students.push(message);
      }

      response.send(200, `${students.join('\n')}`);
    })
    .catch(() => {
      response.send(500, 'Cannot load the database');
    });
  }

  static getAllStudentsByMajor(request, response, db) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.send(500, 'Major parameter must be CS or SWE');
    } else {
      readDatabase(db)
      .then((fields) => {
        const studens = fields[major];

        response.send(200, `List: ${students.join(', ')}`);
      })
      .catch(() => {
        response.send(500, 'Cannot load the database');
      })
    }
  }
}
