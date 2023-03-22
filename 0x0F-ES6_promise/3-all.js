import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  const photo = uploadPhoto();
  const userData = createUser();

  photo.then((response) => {
    process.stdout.write(response.body);
  }).catch(() => {
    console.log('Signup system offline');
  });

  userData.then((response) => {
    console.log(` ${response.firstName} ${response.lastName}`);
  }).catch(() => {
    console.log('Signup system offline');
  });
}

export default handleProfileSignup;
