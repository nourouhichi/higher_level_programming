#!/usr/bin/node
let num = process.argv[2];
num = parseInt(num);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
