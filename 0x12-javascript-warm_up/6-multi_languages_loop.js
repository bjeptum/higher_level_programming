#!/usr/bin/node
// Prints  3 lines using array and loop
const msg = [];
msg.push('C is fun', 'Python is cool', 'JavaScript is amazing');
const len = msg.length;
for (let i = 0; i < len; i++) {
  console.log(msg[i]);
}
