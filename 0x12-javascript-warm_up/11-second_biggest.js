#!/usr/bin/node
// Searches for second biggest integr in the list of arguments
const process = require('process');
const args = process.argv.slice(2);
function secondBiggest (args) {
  const n = args.length;
  if (n < 2) {
    return 0;
  }
  args.sort();
  let i;
  for (i = n - 2; i >= 0; i--) {
    if (args[i] !== args[n - 1]) {
      return args[i];
    }
  }
}
console.log(secondBiggest(args));
