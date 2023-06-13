#!/usr/bin/node
/*
Function that increments and calls a function
Function is visible from outside
*/
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}
module.exports.addMeMaybe = function (number, theFunction) {
  addMeMaybe(number, theFunction);
};
