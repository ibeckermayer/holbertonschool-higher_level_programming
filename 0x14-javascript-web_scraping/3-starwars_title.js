#!/usr/bin/node

const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
