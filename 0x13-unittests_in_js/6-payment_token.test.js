const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
    it('async test', (done) => {
        getPaymentTokenFromAPI(true)
        .then((res) => {
            expect(res).to.include({data: 'Successful response from the API' });
            done();
        })
        .catch((error) => {
            done(error);
        })
    })
})