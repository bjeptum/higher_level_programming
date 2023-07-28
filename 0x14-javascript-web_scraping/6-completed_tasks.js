#!/usr/bin/node
/*
Computes the number of tasks completed by user id
*/
const request = require('request');

function getUsersWithCompletedTasks (url) {
  // Get all todo tasks from the API
  request.get(url, (error, response, todosData) => {
    if (error) {
      console.error('Error fetching todo list:', error);
      return;
    }

    const todos = JSON.parse(todosData);
    const usersCompletedTasks = {};

    // Count completed tasks for each user ID
    todos.forEach(({userId, completed }) => {
      if (completed) {
		  usersCompletedTasks[userId] = (usersCompletedTasks[userId] || 0) + 1;
	  }
	});
    console.log(usersCompletedTasks);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: script_name.js url');
  process.exit(1);
}

const url = process.argv[2];
getUsersWithCompletedTasks(url);
