#!/usr/bin/node

// Get the URL from the command line arguments
const request = require('request');

request(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode); // Print the response status code if a response was received
});
