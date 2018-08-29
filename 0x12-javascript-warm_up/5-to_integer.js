#!/usr/bin/node
let a = process.argv.slice(2);
if (isNaN(Number(a[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(a[0]));
}
