#!/usr/bin/node
function factorial (a) {
  if (a === 0) return 1;
  return a * factorial(a - 1);
}
let n1 = isNaN(Number(process.argv[2])) ? 1 : Number(process.argv[2]);
console.log(factorial(n1));
