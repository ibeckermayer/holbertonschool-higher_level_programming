#!/usr/bin/node
let n = process.argv.slice(2).map(x => Number(x));
if (n.length <= 1) {
  console.log(0);
} else {
  console.log(n.sort().reverse()[1]);
}
