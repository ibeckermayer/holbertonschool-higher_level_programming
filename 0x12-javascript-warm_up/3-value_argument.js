#!/usr/bin/node
let a = process.argv.slice(2);
if (a[0] === undefined) {
  console.log('No argument');
} else {
  console.log(a[0]);
}
