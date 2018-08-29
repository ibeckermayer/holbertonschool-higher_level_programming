#!/usr/bin/node
let a = process.argv[2];
if (isNaN(Number(a))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(a); i++) {
    console.log('X'.repeat(a));
  }
}
