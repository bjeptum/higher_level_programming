#!/usr/bin/node
/*
 Increments a function and calls it
 Function must be visible from outside
*/
function addFunction (number, theFunction) {
  if (number <= 0) {
    return;
  }
  number++;
  theFunction(number);
}
module.exports.addMeMaybe = function (number, theFunction) {
  addFunction(number, theFunction);
};
