#!/usr/bin/node
/*
Imports an array and computes a new array
*/
const list = require('./100-data').list;
const newArray = list.map((num, index) => {
  return (num * index);
});
console.log(list);
console.log(newArray);
