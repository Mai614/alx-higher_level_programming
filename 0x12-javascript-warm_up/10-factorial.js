#!/usr/bin/node
// computes and prints a factorial

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
}
const input = parseInt(process.argv[2]);
const result = factorial(input);
console.log(result);
