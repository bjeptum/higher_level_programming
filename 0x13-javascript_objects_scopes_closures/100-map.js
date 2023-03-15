#!/usr/bin/node
/*
 Imports an array and computes a new array
 must import list from the file 100-data.js
 Print both the initial list and the new list
*/
const list = require('./100-data').list;

const newList = list.map((value, index) => value * index);

console.log('Initial list: ', list);
console.log('New list: ', newList);
