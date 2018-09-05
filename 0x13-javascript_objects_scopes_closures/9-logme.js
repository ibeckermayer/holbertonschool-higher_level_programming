#!/usr/bin/node

let AlreadyPrinted = 0;
exports.logMe = function (item) {
  console.log(AlreadyPrinted + ': ' + item);
  AlreadyPrinted += 1;
};
