#!/usr/bin/node
let n1 = process.argv[2];
let n2 = process.argv[3];
function add (a, b) {
  return (a + b);
}

console.log(add(Number(n1), Number(n2)));
