#!/usr/bin/node
/*
Concats files
*/
const process = require('process');
const myArgs = process.argv;
const arg1 = myArgs[2];
const arg2 = myArgs[3];
const arg3 = myArgs[4];

const { FilesManager } = require('turbodepot-node');
let filesManager = new FilesManager();
filesManager.mergeFiles(['arg1', 'arg2'], 'arg3', "\n");
