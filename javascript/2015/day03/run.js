const utils = require('../../utils');
const tasks = require('./tasks');

const data = utils.getData()[0];

console.log('Task 1: ', tasks.task1(data));
console.log('Task 2: ', tasks.task2(data));