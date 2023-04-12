const calculateNumber = require('./2-calcul_chai');
const { expect } = require('chai');


describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return 5 when type is SUM a is 1 and b is 4', () => {
            expect(calculateNumber('SUM', 1, 4)).to.equal(5);
        })
        it('should return 5 when type is SUM a is 1 and b is 4.2', () => {
            expect(calculateNumber('SUM', 1, 4.2)).to.equal(5);
        })
        it('should return 6 when type is SUM a is 1 and b is 4.5', () => {
            expect(calculateNumber('SUM', 1, 4.5)).to.equal(6);
        })
        it('should return 5 when type is SUM a is 1.2 and b is 4', () => {
            expect(calculateNumber('SUM', 1.2, 4)).to.equal(5);
        })
        it('should return 6 when type is SUM a is 1.5 and b is 4', () => {
            expect(calculateNumber('SUM', 1.5, 4)).to.equal(6);
        })
        it('should return 5 when type is SUM a is 1.2 and b is 4.2', () => {
            expect(calculateNumber('SUM', 1.2, 4.2)).to.equal(5);
        })
        it('should return 7 when type is SUM a is 1.5 and b is 4.6', () => {
            expect(calculateNumber('SUM', 1.5, 4.6)).to.equal(7);
        })
    })
    describe('SUBTRACT', () => {
        it('should return -3 when type is SUBTRACT a is 1 and b is 4', () => {
            expect(calculateNumber('SUBTRACT', 1, 4)).to.equal(-3);
        })
        it('should return -3 when type is SUBTRACT a is 1 and b is 4.2', () => {
            expect(calculateNumber('SUBTRACT', 1, 4.2)).to.equal(-3);
        })
        it('should return -4 when type is SUBTRACT a is 1 and b is 4.5', () => {
            expect(calculateNumber('SUBTRACT', 1, 4.5)).to.equal(-4);
        })
        it('should return -3 when type is SUBTRACT a is 1.2 and b is 4', () => {
            expect(calculateNumber('SUBTRACT', 1.2, 4)).to.equal(-3);
        })
        it('should return -2 when type is SUBTRACT a is 1.5 and b is 4', () => {
            expect(calculateNumber('SUBTRACT', 1.5, 4)).to.equal(-2);
        })
        it('should return -3 when type is SUBTRACT a is 1.2 and b is 4.2', () => {
            expect(calculateNumber('SUBTRACT', 1.2, 4.2)).to.equal(-3);
        })
        it('should return -4 when type is SUBTRACT a is 1.5 and b is 4.5', () => {
            expect(calculateNumber('SUBTRACT', 1.5, 4.6)).to.equal(-3);
        })
    })
    describe('DIVIDE', () => {
        it('should return 0.25 when type is DIVIDE a is 1 and b is 4', () => {
            expect(calculateNumber('DIVIDE', 1, 4)).to.equal(0.25);
        })
        it('should return 0.25 when type is DIVIDE a is 1 and b is 4.2', () => {
            expect(calculateNumber('DIVIDE', 1, 4.2)).to.equal(0.25);
        })
        it('should return 0.2 when type is DIVIDE a is 1 and b is 4.5', () => {
            expect(calculateNumber('DIVIDE', 1, 4.5)).to.equal(0.2);
        })
        it('should return 0.25 when type is DIVIDE a is 1.2 and b is 4', () => {
            expect(calculateNumber('DIVIDE', 1.2, 4)).to.equal(0.25);
        })
        it('should return 0.5 when type is DIVIDE a is 1.5 and b is 4', () => {
            expect(calculateNumber('DIVIDE', 1.5, 4)).to.equal(0.5);
        })
        it('should return 0.25 when type is DIVIDE a is 1.2 and b is 4.2', () => {
            expect(calculateNumber('DIVIDE', 1.2, 4.2)).to.equal(0.25);
        })
        it('should return 0.4 when type is DIVIDE a is 1.5 and b is 4.5', () => {
            expect(calculateNumber('DIVIDE', 1.5, 4.6)).to.equal(0.4);
        })
        it('should return Error when type is DIVIDE a is 1.2 and b is 0', () => {
            expect(calculateNumber('DIVIDE', 1.2, 0)).to.equal('Error');
        })
        it('should return Error when type is DIVIDE a is 1.5 and b is 0', () => {
            expect(calculateNumber('DIVIDE', 1.5, 0)).to.equal('Error');
        })
        it('should return Error when type is DIVIDE a is 1 and b is 0', () => {
            expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
        })
    })
});
