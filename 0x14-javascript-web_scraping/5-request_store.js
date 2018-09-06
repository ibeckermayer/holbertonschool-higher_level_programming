#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
