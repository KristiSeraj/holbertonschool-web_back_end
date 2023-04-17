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


describe('express server regex integration testing', () => {
    it('GET /cart/:id', (done) => {
        const call = {
            url: 'http://localhost:7865/cart/12',
            method: 'GET'
        };
        request(call, (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    })
})

describe('express server regex integration testing', () => {
    it('GET /cart/isNaN', (done) => {
        const call = {
            url: 'http://localhost:7865/cart/hello',
            method: 'GET'
        };
        request(call, (err, res, body) => {
            expect(res.statusCode).to.equal(404);
            done();
        });
    })
})


describe('express server regex integration testing', () => {
    it('GET /available_payments', (done) => {
        const call = {
            url: 'http://localhost:7865/available_payments',
            method: 'GET'
        };
        request(call, (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            expect(body).to.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
            done();
        });
    })
})


describe('express server regex integration testing', () => {
    it('POST /login', (done) => {
        const call = {
            url: 'http://localhost:7865/login',
            method: 'POST',
            json: {
                userName: 'Betty'
            }
        };
        request(call, (err, res, body) => {
            expect(res.statusCode).to.equal(200);
            expect(body).to.equal('Welcome Betty');
            done();
        });
    })
})
