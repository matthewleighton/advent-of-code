const utils = require('../../utils');
const funcs = require('./funcs');

const data = utils.getData();

const task1 = funcs.solveTask(data, 1);
console.log('Task 1', task1);

const task2 = funcs.solveTask(data, 2);
console.log('Task 1', task2);