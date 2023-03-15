#!/usr/bin/node
/*
 Converts number to another base in argument from base 10
*/
exports.converter = function (base) {
  return function (num) {
    return (num.toString(base));
  };
};
