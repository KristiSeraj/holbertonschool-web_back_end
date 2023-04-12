const sinon = require('sinon');
const Utils = require('./utils');
const assert = require('assert');
const sendPaymentRequestToApi = require('./4-payment');

describe('Payment', () => {
    it('should validate sendPaymentRequestToApi', () => {
        const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const consoleLogSpy = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);
        assert(calculateNumberStub.calledWithExactly('SUM', 100, 20));
        assert(consoleLogSpy.calledWithExactly('The total is: 10'));
        calculateNumberStub.restore();
        consoleLogSpy.restore();
    })
})