const readDatabase = require('../utils');

export default class StudentController {
  static getAllStudents(request, response, db) {
    readDatabase(db)
    .then((fields) => {
      const students = [];
      let message;
      students.push('This is the list of our students');

      for (const key of Object.keys(fields)) {
        message = `Number of students in ${key}: ${fields[key].length}. List ${fields[key].join(', ')}`;
        students.push(message);
      }

      response.status(200).send(`${students.join('\n')}`);
    })
    .catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }

  static getAllStudentsByMajor(request, response, db) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
    } else {
      readDatabase(db)
      .then((fields) => {
        const studentsMajor = fields[major];

        response.status(200).send(`List: ${studentsMajor.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      })
    }
  }
}
