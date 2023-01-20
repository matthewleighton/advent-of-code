const utils = require('../../utils');
const funcs = require('./funcs');

const data = utils.getData();

const task1 = funcs.solveTask1(data);
console.log('Task 1', task1);