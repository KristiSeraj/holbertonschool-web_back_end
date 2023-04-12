const assert = require('assert');
const calculateNumber = require('./0-calcul');


describe('calculateNumber', () => {
    it('should return 4 when a is 1 and b is 3', () => {
        assert.equal(calculateNumber(1, 3), 4);
    });
});
