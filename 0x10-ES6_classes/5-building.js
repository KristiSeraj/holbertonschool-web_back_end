export default class Building {
  constructor(sqrt) {
    if (typeof sqrt !== 'number') throw new Error('Sqrt must be a number');
    this._sqrt = sqrt;
  }

  get sqrt() {
    return this._sqrt;
  }

  /*eslint-disable */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
