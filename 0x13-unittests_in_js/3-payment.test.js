const sinon = require('sinon');
const Utils = require('./utils');
const assert = require('assert');
const sendPaymentRequestToApi = require('./3-payment');

describe('Payment', () => {
    it('should validate sendPaymentRequestToApi', () => {
        const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 200);
        assert(calculateNumberSpy.calledWith('SUM', 100, 200));
        calculateNumberSpy.restore();
    })
})