#!/usr/bin/node
/*
Imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence
*/
const dict = require('./101-data').dict;
const users = {};

for (const userId in dict) {
  const count = dict[userId];
  if (!(count in users)) {
    users[count] = [];
  }
  users[count].push(userId);
}
console.log(users);
