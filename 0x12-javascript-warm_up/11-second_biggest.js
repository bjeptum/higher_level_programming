#!/usr/bin/node
// Searches for second biggest integer in the list of arguments
const process = require('process');
const args = process.argv.slice(2);
function secondBiggest (args) {
  const n = args.length;
  if (n < 2) {
    return 0;
  }
  args.sort((a, b) => parseInt(b) - parseInt(a));
  let i;
  for (i = 1; i < n; i++) {
    if (args[i] !== args[0]) {
      return args[i];
    }
  }
}
console.log(secondBiggest(args));
