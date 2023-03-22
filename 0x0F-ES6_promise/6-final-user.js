import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
    let param1 = signUpUser(firstName, lastName);
    let param2 = uploadPhoto(fileName);

    console.log([param1, param2]);
}