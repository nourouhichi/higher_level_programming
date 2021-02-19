#!/usr/bin/node
const arg = process.argv;
const size = arg.length;
if (size <= 3) {
  console.log(0);
} else {
  arg.sort(function (a, b) {
    return a - b;
  });
  const second = arg[size - 2];
  console.log(second);
}
