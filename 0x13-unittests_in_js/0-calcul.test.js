const assert = require('assert');
const calculateNumber = require('./0-calcul');


describe('calculateNumber', () => {
    it('should return 4 when a is 1 and b is 3', () => {
        assert.equal(calculateNumber(1, 3), 4);
    });
    it('should return 5 when a is 1 and b is 3.7', () => {
        assert.equal(calculateNumber(1, 3.7), 5);
    });
    it('should return 5 when a is 1.2 and b is 3.7', () => {
        assert.equal(calculateNumber(1.2, 3.7), 5);
    });
    it('should return 6 when a is 1.5 and b is 3.7', () => {
        assert.equal(calculateNumber(1.5, 3.7), 6);
    });
});
