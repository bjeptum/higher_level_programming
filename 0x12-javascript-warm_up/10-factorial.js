#!/usr/bin/node
/*
 Function that computes and prints factorial
 The first argument is integer (argument can be cast as integer) used for computing the factorial
 Factorial of NaN is 1
 Apply recursion
 Use console.log(...) to print all output
 No use var
 */
function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const value = parseInt(process.argv[2]);
console.log(factorial(value));
