#!/usr/bin/node
/*
Executes x time the function
Function is visible from outside it
*/
function callMeMoby (x, theFunction) {
  if (x <= 0) {
    return;
  }
  theFunction();
  callMeMoby(x - 1, theFunction);
}
module.exports.callMeMoby = callMeMoby;
