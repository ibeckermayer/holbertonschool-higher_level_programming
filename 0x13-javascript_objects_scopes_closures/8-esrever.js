#!/usr/bin/node

exports.esrever = function (list) {
  let final = Array(list.length);
  for (let i = 0; i < list.length; i++) {
    final[i] = list[list.length - 1 - i];
  }
  return final;
};
