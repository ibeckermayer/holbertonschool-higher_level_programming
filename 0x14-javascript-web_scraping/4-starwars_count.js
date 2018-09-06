#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    let res = JSON.parse(body).results;
    let cnt = 0;
    for (let i = 0; i < res.length; i++) {
      let chars = res[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes('/18/')) {
          cnt += 1;
        }
      }
    }
    console.log(cnt);
  }
});
