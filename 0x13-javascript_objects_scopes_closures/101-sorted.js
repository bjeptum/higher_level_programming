#!/usr/bin/node
/*
 Imports a dictionary of occurrences by user id
 Then computes a dictionary of user ids by occurrence
*/
const dict = require('./101-data').dict;

const result = {};

/* Iterate through the keys of the original dictionary */
for (const userId in dict) {
  const occurrenceCount = dict[userId];

  /* If the number of occurrences is not already a key in the result dictionary,
 create a new key with an empty array as the value
*/
  if (!(occurrenceCount in result)) {
    result[occurrenceCount] = [];
  }

  /* Add the current user ID to the array for the number of occurrences */
  result[occurrenceCount].push(userId);
}

console.log(result);
