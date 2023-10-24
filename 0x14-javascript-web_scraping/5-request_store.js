#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// gets the contents of a webpage and stores it in a file

request(process.argv[2], function (_err, _res, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
