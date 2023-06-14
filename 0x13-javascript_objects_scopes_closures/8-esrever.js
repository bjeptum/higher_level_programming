#!/usr/bin/node
/*
Returns reverser version of list
*/
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return reverseList;
};
