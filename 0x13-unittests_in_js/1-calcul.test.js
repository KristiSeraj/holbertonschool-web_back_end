const assert = require('assert');
const calculateNumber = require('./1-calcul');


describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return 5 when type is SUM a is 1 and b is 4', () => {
            assert.equal(calculateNumber('SUM', 1, 4), 5);
        })
        it('should return 5 when type is SUM a is 1 and b is 4.2', () => {
            assert.equal(calculateNumber('SUM', 1, 4.2), 5);
        })
        it('should return 6 when type is SUM a is 1 and b is 4.5', () => {
            assert.equal(calculateNumber('SUM', 1, 4.5), 6);
        })
        it('should return 5 when type is SUM a is 1.2 and b is 4', () => {
            assert.equal(calculateNumber('SUM', 1.2, 4), 5);
        })
        it('should return 6 when type is SUM a is 1.5 and b is 4', () => {
            assert.equal(calculateNumber('SUM', 1.5, 4), 6);
        })
        it('should return 5 when type is SUM a is 1.2 and b is 4.2', () => {
            assert.equal(calculateNumber('SUM', 1.2, 4.2), 5);
        })
        it('should return 7 when type is SUM a is 1.5 and b is 4.6', () => {
            assert.equal(calculateNumber('SUM', 1.5, 4.6), 7);
        })
    })
    describe('SUBTRACT', () => {
        it('should return -3 when type is SUBTRACT a is 1 and b is 4', () => {
            assert.equal(calculateNumber('SUBTRACT', 1, 4), -3);
        })
        it('should return -3 when type is SUBTRACT a is 1 and b is 4.2', () => {
            assert.equal(calculateNumber('SUBTRACT', 1, 4.2), -3);
        })
        it('should return -4 when type is SUBTRACT a is 1 and b is 4.5', () => {
            assert.equal(calculateNumber('SUBTRACT', 1, 4.5), -4);
        })
        it('should return -3 when type is SUBTRACT a is 1.2 and b is 4', () => {
            assert.equal(calculateNumber('SUBTRACT', 1.2, 4), -3);
        })
        it('should return -2 when type is SUBTRACT a is 1.5 and b is 4', () => {
            assert.equal(calculateNumber('SUBTRACT', 1.5, 4), -2);
        })
        it('should return -3 when type is SUBTRACT a is 1.2 and b is 4.2', () => {
            assert.equal(calculateNumber('SUBTRACT', 1.2, 4.2), -3);
        })
        it('should return -4 when type is SUBTRACT a is 1.4 and b is 4.5', () => {
            assert.equal(calculateNumber('SUBTRACT', 1.5, 4.6), -3);
        })
    })
});
