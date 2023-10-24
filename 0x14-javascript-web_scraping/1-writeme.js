#!/usr/bin/node

const fs = require('fs');

// Get file path and string to write from command line arguments
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
