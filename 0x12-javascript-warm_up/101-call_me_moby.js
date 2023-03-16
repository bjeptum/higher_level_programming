#!/usr/bin/node
/*
 Executes x times a function
 Function must be visible from outside
*/
function repeatFunction (x, theFunction) {
  if (x <= 0) {
    return;
  }
  theFunction();
  repeatFunction(x - 1, theFunction);
}

module.exports.callMeMoby = function (x, theFunction) {
  repeatFunction(x, theFunction);
};
