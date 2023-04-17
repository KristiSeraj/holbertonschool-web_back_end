const request = require('request');
const { expect } = require('chai');

describe('express server', () => {
    it('GET /', (done) => {
        const call = {
            url: 'http://localhost:7865',
            method: 'GET'
        };
        request(call, (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    })
})