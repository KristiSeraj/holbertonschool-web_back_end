export default class AppController {
  static getHomepage(request, response) {
    response.status(200).send('Hello Hoblerton School!');
  }
}
