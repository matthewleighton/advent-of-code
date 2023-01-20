const funcs = require('./funcs');
const utils = require('../../utils');

key = utils.getData()[0];

task1 = funcs.solveTask(key, 5);
console.log('Task 1:', task1);

task2 = funcs.solveTask(key, 6);
console.log('Task 1:', task2);