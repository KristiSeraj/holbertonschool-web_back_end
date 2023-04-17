const sinon = require('sinon');
const Utils = require('./utils');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('Payment', () => {
    let spyConsole;

    beforeEach(() => {
        spyConsole = sinon.spy(console, 'log');
    })
    afterEach(() => {
        spyConsole.restore();
    })

    it('should call sendPaymentRequestToApi with 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);
        expect(spyConsole.calledOnce).to.be.true;
        expect(spyConsole.calledWith('The total is: 120')).to.be.true;
    })
    it('should vcall sendPaymentRequestToApi with 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);
        expect(spyConsole.calledOnce).to.be.true;
        expect(spyConsole.calledWith('The total is: 20')).to.be.true;
    })
})